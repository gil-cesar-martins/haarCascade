✨ Funcionalidades Principais
Detecção de Faces: Utiliza o classificador pré-treinado haarcascade_frontalface_default.xml do OpenCV para localizar faces em imagens.

Painel de Controle Interativo: Permite o ajuste fino em tempo real dos hiperparâmetros do detector Haar Cascade:

scaleFactor: Fator de escala da imagem em cada passo da detecção.

minNeighbors: Nível de confiança para validar uma detecção de face.

minSize: O menor tamanho de face (em pixels) a ser considerado.

Duas Fontes de Imagem: O usuário pode optar por fazer o upload de suas próprias imagens (JPG, PNG, JPEG) ou selecionar imagens de exemplo pré-carregadas na pasta imagens/.

Interface Educacional: Uma aba dedicada ("Como o Algoritmo Funciona?") explica os conceitos teóricos por trás do Haar Cascade de forma clara e acessível.

Comparação Visual: Exibe a imagem original e a imagem com as detecções lado a lado para uma fácil comparação dos resultados.

Branding Customizado: Demonstra como adicionar uma logomarca e personalizar a interface do Streamlit.

🛠️ Tecnologias Utilizadas
Backend & Lógica de CV: Python

Interface Web: Streamlit

Processamento de Imagem: OpenCV-Python

Manipulação de Imagem: Pillow (PIL)

Operações Numéricas: NumPy

⚙️ Configuração e Instalação
Para executar este projeto localmente, siga os passos abaixo:

1. Pré-requisitos:

Python 3.9 ou superior instalado.

pip (gerenciador de pacotes do Python).

2. Clone o Repositório:

Bash

git clone https://github.com/gil-cesar-martins/haarCascade.git
cd seu-repositorio

3. Crie e Ative um Ambiente Virtual (Recomendado):

Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
macOS / Linux:

Bash

python3 -m venv venv
source venv/bin/activate

4. Instale as Dependências:
Crie um arquivo chamado requirements.txt na raiz do projeto com o seguinte conteúdo:

Plaintext

streamlit
opencv-python-headless
numpy
Pillow
Em seguida, instale as bibliotecas com o comando:

Bash

pip install -r requirements.txt


🚀 Como Executar a Aplicação
Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no terminal:

Bash

streamlit run app.py
Seu navegador abrirá automaticamente no endereço http://localhost:8501 com a aplicação em execução.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido com o objetivo de aprender e demonstrar as capacidades da Visão Computacional de forma prática e interativa.
