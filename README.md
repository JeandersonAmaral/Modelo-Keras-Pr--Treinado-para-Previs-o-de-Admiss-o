# 🎓 Sistema de Previsão de Admissão com Keras

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

O projeto adota uma estrutura padrão para aplicações Python, garantindo clareza e escalabilidade.

Fechado! Um bom README é o cartão de visitas de um projeto no GitHub. Ele precisa ser claro, informativo e ter um visual legal.

Preparei um template completo usando Markdown, com badges, emojis e uma estrutura profissional. É só copiar, colar em um arquivo README.md na raiz do seu projeto e preencher seus dados.

Como Ficaria o README.md
Markdown

# 🎓 Sistema de Previsão de Admissão com Keras

![Linguagem](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Framework](https://img.shields.io/badge/Keras-TensorFlow-red?style=for-the-badge&logo=keras)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licença-MIT-brightgreen?style=for-the-badge)

<p align="center">
  Um script interativo de linha de comando (CLI) que utiliza um modelo de rede neural pré-treinado para prever a probabilidade de admissão de um candidato em uma universidade.
</p>

---

## 演示 (Demonstração)

Veja o sistema em ação no modo de previsão manual. A interface é colorida para facilitar a leitura e o uso.

![Demonstração em GIF do Terminal](https://i.imgur.com/vHq8z7p.gif)
*(Este é um exemplo de GIF, você pode criar um do seu terminal usando ferramentas como ScreenToGif ou Kap)*

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

O projeto adota uma estrutura padrão para aplicações Python, garantindo clareza e escalabilidade.

projeto/
│
├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git
├── README.md           # Esta documentação
├── requirements.txt    # Lista de dependências do projeto
├── run.py              # Ponto de entrada para executar a aplicação
│
├── data/
│   ├── modelo_treinado.keras   # O modelo pré-treinado
│   └── dados_candidatos.csv    # Dados de exemplo para previsão em lote
│
├── src/
│   └── previsao_admissao/
│       ├── init.py
│       ├── main.py             # Orquestra a lógica da aplicação
│       ├── gerenciador_modelo.py # Lógica para carregar e usar o modelo
│       └── interface_usuario.py  # Lógica para a interface de linha de comando
│


---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto localmente.

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
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

📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

<p align="center">
Feito com ❤️ por <strong>[SEU NOME AQUI]</strong>
</p>
<p align="center">
<a href="https://www.google.com/search?q=https://github.com/SEU_USUARIO">GitHub</a> •
<a href="https://www.google.com/search?q=https://www.linkedin.com/in/SEU_LINKEDIN/">LinkedIn</a>

</p>
