from colorama import Fore, Style
from .gerenciador_modelo import carregar_modelo_pre_treinado
from .interface_usuario import modo_manual, processar_arquivo_csv

def run_app():
    """
    Função principal que executa a lógica da aplicação.
    """
    CAMINHO_MODELO = 'data/modelo_treinado.keras'
    modelo = carregar_modelo_pre_treinado(CAMINHO_MODELO)
    
    if not modelo:
        return

    while True:
        print(Style.BRIGHT + Fore.CYAN + "\nO que você deseja fazer?")
        print(Fore.CYAN + "  1 - Prever a chance de um único candidato (manual)")
        print(Fore.CYAN + "  2 - Prever a chance de múltiplos candidatos (via CSV)")
        print(Fore.CYAN + "  3 - Sair")
        
        escolha = input(Style.BRIGHT + Fore.CYAN + "Digite sua escolha (1, 2 ou 3): ")
        
        if escolha == '1':
            modo_manual(modelo)
        elif escolha == '2':
            processar_arquivo_csv(modelo)
        elif escolha == '3':
            print(Fore.GREEN + "Programa finalizado.")
            break
        else:
            print(Fore.RED + "\n[ERRO] Opção inválida. Por favor, escolha 1, 2 ou 3.")