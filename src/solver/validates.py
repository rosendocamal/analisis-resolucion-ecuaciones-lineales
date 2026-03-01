# Funciones de validación de entrada del usuario

def validate_num_input(msg: str) -> float:
    """
    Solicita un número al usuario y si la entrada
    es un número retorna el resultado, sino 
    la función insiste en ello.

    Parámetros:
    msg (str): Instrucción para solicitar el número.

    Retorna:
    num (float): El número ingresado por el usuario.
    
    Excepciones:
    ValueError: Si el dato no es un número.
    """
    while True:
        try:
            num: float = float(input(msg).strip())
        except ValueError:
            print('Error: Entrada inválida. Por favor, introduzca un número válido.')
        else:
            return num

def validate_option() -> int:
    """
    Solicita un número (opción) al usuario y si la entrada
    es un número entero del 1 al 4, retorna el
    resultado, de lo contrario, la función
    insiste en ello.

    Retorna:
    option (int): Es la opción ingresada por el usuario.

    Excepciones:
    ValueError: Si el dato ingresado no es un número.
    """
    msg: str = 'Error: Opción inválida. Por favor, introduzca un número del 1 al 4.'
    while True:
        try:
            option: int = int(input('Selecione una opción: '))

            if option not in {1, 2, 3, 4}:
                print(msg)
                continue
        except ValueError:
            print(msg)
        else:
            print()
            return option