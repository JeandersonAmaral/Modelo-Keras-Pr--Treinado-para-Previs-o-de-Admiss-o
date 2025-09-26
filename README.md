# 🎓 Previsão de Admissão com Keras

![Linguagem](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Framework](https://img.shields.io/badge/Keras-TensorFlow-red?style=for-the-badge&logo=keras)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licença-MIT-brightgreen?style=for-the-badge)

<p align="center">
  Um script interativo de linha de comando (CLI) que utiliza um modelo de rede neural pré-treinado para prever a probabilidade de admissão de um candidato em uma universidade.
</p>

---

## ✨ Funcionalidades Principais

-   🔮 **Previsão Interativa:** Insira os dados de um candidato manualmente e receba a previsão de admissão em tempo real.
-   📄 **Previsão em Lote:** Carregue um arquivo `.csv` com múltiplos candidatos e receba uma tabela completa com as previsões.
-   🎨 **Interface Colorida:** Saídas no terminal com cores para melhor legibilidade, usando a biblioteca `colorama`.
-   🏗️ **Arquitetura Modular:** O projeto é organizado de forma limpa e profissional, separando as responsabilidades em diferentes módulos.
-   🐍 **Ambiente Virtual:** Script pronto para ser executado em um ambiente Python isolado para gerenciamento limpo de dependências.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído com as seguintes tecnologias e bibliotecas:

-   **Python**
-   **TensorFlow / Keras:** Para carregar e utilizar o modelo de rede neural.
-   **Pandas:** Para manipulação e leitura de dados do arquivo CSV.
-   **NumPy:** Para operações numéricas eficientes.
-   **Colorama:** Para estilizar a saída do terminal com cores.

---

## 📂 Estrutura do Projeto

```text
O projeto adota uma estrutura padrão para aplicações Python, garantindo clareza e escalabilidade.

📁 projeto_final/
┣━━ 🚀 run.py                  # Ponto de entrada para executar a aplicação
┣━━ 📄 requirements.txt       # Lista de dependências para instalação
┣━━ 📖 README.md                # Esta documentação
┣━━ 🔑 .gitignore                # Arquivos ignorados pelo Git
┣━━ 📂 data/
┃   ┣━━ 🧠 modelo_treinado.keras  # O modelo de rede neural pré-treinado
┃   ┗━━ 📊 dados_candidatos.csv   # Dados de exemplo para previsão em lote
┣━━ 📂 src/
┃   ┗━━ 📂 previsao_admissao/
┃       ┣━━ 📜 __init__.py         # Inicializa o pacote Python
┃       ┣━━ 📜 main.py            # Orquestra a lógica da aplicação (menu)
┃       ┣━━ 📜 gerenciador_modelo.py # Carrega e utiliza o modelo Keras
┃       ┗━━ 📜 interface_usuario.py  # Controla a interação com o usuário

```

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto localmente.

```bash
1. Clone o repositório:

git clone https://github.com/JeandersonAmaral/Previsao-de-Admissao-com-Keras
cd NOME_DO_REPOSITORIO

2. Crie e ative um ambiente virtual:

# Crie o ambiente
python -m venv venv

# Ative o ambiente
# Windows:
.\venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate

3. Instale as dependências:

pip install -r requirements.txt

4. Adicione o modelo:
Faça o download do arquivo modelo_treinado.keras e coloque-o dentro da pasta data/.

5. Execute a aplicação:

python run.py

O menu interativo irá guiá-lo a partir daqui!





