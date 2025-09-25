import os
from keras.models import load_model

def carregar_modelo_pre_treinado(caminho_modelo):
    if not os.path.exists(caminho_modelo):
        print(f"\nERRO CRÍTICO: O arquivo do modelo '{caminho_modelo}' não foi encontrado!")
        return None
    
    print(f"Carregando o modelo de '{caminho_modelo}'...")
    try:
        modelo = load_model(caminho_modelo)
        print("Modelo carregado com sucesso!")
        return modelo
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o modelo: {e}")
        return None

def fazer_previsao(modelo, dados_entrada):
    print("Gerando previsão(ões)...")
    try:
        previsoes = modelo.predict(dados_entrada)
        return previsoes
    except Exception as e:
        print(f"Ocorreu um erro ao realizar a previsão: {e}")
        return None