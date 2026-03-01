# Orquestador final del CLI

from src.solver import cli
from src.solver import testing

def run_test() -> None:
    """
    Permite acceder a las pruebas de test
    """

    testing.run_test()

def run_menu() -> None:
    """
    Permite acceder al programa principal
    """
    
    cli.menu()

if __name__ == '__main__':
    # Ejecutar pruebas de código
    try:
        run_test()
    except AssertionError:
        print('>>> El programa no logró pasar las pruebas.')
    else:
        print('>>> El programa si logró pasar las pruebas.')
        run_menu()