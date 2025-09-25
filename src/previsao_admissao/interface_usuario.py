import os
import numpy as np
import pandas as pd
from colorama import Fore, Style
from .gerenciador_modelo import fazer_previsao

def modo_manual(modelo):
    colunas_regras = [
        {'nome': 'GRE Score', 'min': 260, 'max': 340, 'tipo': int},
        {'nome': 'TOEFL Score', 'min': 0, 'max': 120, 'tipo': int},
        {'nome': 'University Rating', 'min': 1, 'max': 5, 'tipo': int},
        {'nome': 'SOP', 'min': 1.0, 'max': 5.0, 'tipo': float},
        {'nome': 'LOR', 'min': 1.0, 'max': 5.0, 'tipo': float},
        {'nome': 'CGPA', 'min': 0.0, 'max': 10.0, 'tipo': float},
        {'nome': 'Research', 'min': 0, 'max': 1, 'tipo': int, 'extra': '(0 para Não, 1 para Sim)'}
    ]
    
    valores_usuario = []
    print(Style.BRIGHT + "\n--- Modo Manual: Insira os dados do candidato ---")
    
    for regra in colunas_regras:
        while True:
            try:
                prompt_extra = regra.get('extra', f'entre {regra["min"]} e {regra["max"]}')
                prompt = Fore.GREEN + f"  -> Insira o valor para '{regra['nome']}' {prompt_extra}: "
                valor_str = input(prompt)
                valor = regra['tipo'](valor_str)
                
                if regra['min'] <= valor <= regra['max']:
                    valores_usuario.append(valor)
                    break
                else:
                    print(Fore.RED + f"   [ERRO] Valor fora do intervalo permitido. Tente novamente.")
            except ValueError:
                print(Fore.RED + f"   [ERRO] Entrada inválida. Por favor, insira um número.")

    entrada_para_previsao = np.array([valores_usuario])
    previsao_raw = fazer_previsao(modelo, entrada_para_previsao)
    
    if previsao_raw is not None:
        chance_de_admissao = previsao_raw[0][0]
        # Deixando o resultado bem destacado
        print(Style.BRIGHT + Fore.MAGENTA + "\n==========================================")
        print(Style.BRIGHT + Fore.MAGENTA + "    RESULTADO DA PREVISÃO DE ADMISSÃO")
        print(Style.BRIGHT + Fore.GREEN + f"A chance prevista de admissão é de: {chance_de_admissao:.2%}")
        print(Style.BRIGHT + Fore.MAGENTA + "==========================================")


def processar_arquivo_csv(modelo):
    print(Style.BRIGHT + "\n--- Modo de Previsão em Lote via CSV ---")
    nome_arquivo_csv = input(Fore.GREEN + "Digite o caminho do arquivo CSV (ex: data/dados_candidatos.csv): ")

    if not os.path.exists(nome_arquivo_csv):
        print(Fore.RED + f"\n[ERRO] Arquivo '{nome_arquivo_csv}' não encontrado.")
        return

    try:
        df_candidatos = pd.read_csv(nome_arquivo_csv)
        print(f"Arquivo '{nome_arquivo_csv}' carregado: {len(df_candidatos)} registros encontrados.")

        if len(df_candidatos.columns) != 7:
            print(Fore.RED + f"\n[ERRO] O CSV deve ter 7 colunas. O seu tem {len(df_candidatos.columns)}.")
            return
        
        dados_para_prever = df_candidatos.to_numpy()
        previsoes = fazer_previsao(modelo, dados_para_prever)
        
        if previsoes is not None:
            df_candidatos['Chance of Admit (%)'] = [f"{p[0]:.2%}" for p in previsoes]
            print(Style.BRIGHT + Fore.MAGENTA + "\n================================= RESULTADO DAS PREVISÕES =================================")
            print(Style.BRIGHT + Fore.GREEN + df_candidatos.to_string())
            print(Style.BRIGHT + Fore.MAGENTA + "===========================================================================================")

    except Exception as e:
        print(Fore.RED + f"\n[ERRO] Ocorreu um erro ao processar o arquivo CSV: {e}")