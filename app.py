import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

# ==================================================================================
# 1. FUNÇÃO CORE DE DETECÇÃO DE FACES (Inalterada)
# ==================================================================================
def detect_faces(image_array, scale_factor, min_neighbors, min_size):
    """
    Detecta faces em uma imagem usando o classificador Haar Cascade com parâmetros ajustáveis.
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=(min_size, min_size)
    )
    
    image_with_detections = image_array.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(image_with_detections, (x, y), (x+w, y+h), (0, 255, 255), 3)

    return image_with_detections, len(faces)

# ==================================================================================
# 2. CONFIGURAÇÃO DA PÁGINA E PAINEL DE CONTROLE (SIDEBAR)
# ==================================================================================

st.set_page_config(page_title="Detector de Faces Interativo", page_icon="👤", layout="wide")
st.sidebar.image(".streamlit/logomarca/LOGO_SOLO.png")
st.sidebar.header("🛠️ Painel de Controle")

scale_factor_param = st.sidebar.number_input(
    "Fator de Escala (scaleFactor)", 1.01, 2.0, 1.1, 0.01,
    help="Valores menores (~1.05) detectam mais faces, mas são mais lentos. Valores maiores (~1.4) são mais rápidos, mas podem falhar em detectar faces menores."
)
min_neighbors_param = st.sidebar.number_input(
    "Mínimo de Vizinhos (minNeighbors)", 1, 20, 5, 1,
    help="Controla falsos positivos. Um valor mais alto (e.g., 5-6) resulta em detecções de maior qualidade, mas menos numerosas."
)
min_size_param = st.sidebar.number_input(
    "Tamanho Mínimo da Face (minSize)", 10, 500, 30, 1,
    help="Define o menor rosto a ser detectado em pixels. Ajuda a ignorar 'ruídos' na imagem."
)

run_detection = st.sidebar.button("🚀 Aplicar e Testar", type="primary")



# ==================================================================================
# 3. LAYOUT PRINCIPAL COM ABAS
# ==================================================================================

st.title("👤 Detector de Faces Interativo com Haar Cascade")
st.markdown(" ### Uma aplicação para demonstrar e ensinar os fundamentos da detecção de objetos em Visão Computacional.")

tab1, tab2 = st.tabs(["🧠 Como o Algoritmo Funciona?", "🚀 Demonstração Prática"])

with tab1:
    st.header("O que é o Haar Cascade?")
    st.markdown("""
    O **Haar Cascade** é um algoritmo de detecção de objetos baseado em aprendizado de máquina, proposto por Paul Viola e Michael Jones em 2001. Embora hoje existam métodos mais modernos (como redes neurais convolucionais), ele ainda é um exemplo fantástico dos princípios fundamentais da Visão Computacional.

    Ele funciona através de três conceitos principais:

    1.  **Haar-like Features:** O algoritmo não olha para os pixels individualmente. Em vez disso, ele usa "features" (características) que são basicamente retângulos que medem a diferença de intensidade entre regiões da imagem. Por exemplo, em um rosto, a região dos olhos é geralmente mais escura que a testa e as bochechas.
        
    2.  **Imagem Integral (Integral Image):** Para calcular essas features em toda a imagem de forma extremamente rápida, o algoritmo pré-computa uma estrutura de dados chamada Imagem Integral. Isso permite que a soma dos pixels dentro de qualquer retângulo seja calculada com apenas quatro operações, independentemente do tamanho do retângulo.
        
    3.  **Cascata de Classificadores (Cascade of Classifiers):** O "cascade" no nome vem daqui. Uma janela da imagem passa por uma série de estágios de classificadores. A grande maioria das janelas é descartada nos primeiros estágios (que são mais simples e rápidos), permitindo que o detector foque o poder computacional apenas nas regiões mais promissoras.
    """)

with tab2:
    st.header("Teste o Detector com sua Imagem")
    
    image_to_process = None
    
    source_choice = st.radio(
        "Escolha a fonte da sua imagem:",
        ("Fazer upload da minha imagem", "Selecionar uma imagem de exemplo"),
        horizontal=True,
        label_visibility="collapsed"
    )

    if source_choice == "Fazer upload da minha imagem":
        uploaded_file = st.file_uploader(
            "Arraste e solte uma imagem ou clique para procurar",
            type=["jpg", "jpeg", "png"]
        )
        if uploaded_file:
            image_to_process = Image.open(uploaded_file).convert("RGB")
            
    else: # "Selecionar uma imagem de exemplo"
        IMAGE_DIR = "imagens"
        if not os.path.exists(IMAGE_DIR):
            st.error(f"A pasta '{IMAGE_DIR}' não foi encontrada. Por favor, crie-a no mesmo diretório do app.py.")
            st.stop()
            
        example_images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        if not example_images:
            st.warning(f"Nenhuma imagem encontrada na pasta '{IMAGE_DIR}'. Adicione algumas imagens de exemplo.")
        else:
            selected_image = st.selectbox("Escolha uma imagem de exemplo:", example_images)
            image_path = os.path.join(IMAGE_DIR, selected_image)
            image_to_process = Image.open(image_path).convert("RGB")
    
    col1, col2 = st.columns(2)
    
    if image_to_process:
        with col1:
            st.subheader("🖼️ Imagem Original")
            st.image(image_to_process, use_container_width=True)
            
        img_array = np.array(image_to_process)
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    if run_detection:
        if 'img_bgr' in locals():
            with st.spinner('Analisando a imagem com os novos parâmetros...'):
                result_img, num_faces = detect_faces(
                    image_array=img_bgr,
                    scale_factor=scale_factor_param,
                    min_neighbors=min_neighbors_param,
                    min_size=min_size_param
                )
            
            with col2:
                st.subheader("🔍 Imagem com Detecções")
                result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
                st.image(result_img_rgb, use_container_width=True)
                if num_faces > 0:
                    st.success(f"**{num_faces} face(s) detectada(s)!**")
                else:
                    st.warning("**Nenhuma face foi detectada.** Tente relaxar os parâmetros no Painel de Controle.")
        else:
            st.error("Por favor, carregue uma imagem ou selecione um exemplo primeiro.")