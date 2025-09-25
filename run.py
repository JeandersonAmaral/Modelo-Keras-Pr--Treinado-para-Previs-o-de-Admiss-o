import sys
import os
from colorama import init

init(autoreset=True)

sys.path.append(os.path.abspath('.'))

from src.previsao_admissao.main import run_app

if __name__ == "__main__":
    """
    Ponto de entrada principal da aplicação.
    """
    print("Iniciando a aplicação de Previsão de Admissão...")
    run_app()