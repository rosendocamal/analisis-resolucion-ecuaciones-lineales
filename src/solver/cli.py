# Menú interactivo en aspecto de CLI

from .math import is_linear_equation, solve_simple_linear_eq, solve_linear_system_2x2
from .validates import validate_option, validate_num_input

def menu() -> None:
    """
    Orquestador que maneja el menú en CLI, recibe la opción
    del usuario y ejecuta la preferencia del usuario.
    """

    try:
        while True:
            display_menu()
            option: int = validate_option()

            match option:
                case 1:
                    display_is_linear_equation()
                case 2:
                    display_solve_simple_linear_eq()
                case 3:
                    display_solve_linear_system_2x2()
                case 4:
                    print('Finalizando el programa. ¡Hasta pronto!')
                    break
    except KeyboardInterrupt:
        print('\nFinalizando el programa. ¡Hasta pronto!')
        
def display_menu() -> None:
    """
    Menú de pantalla, solo es la interfaz de texto.
    """

    print()
    print('=' * 50)
    print('\b' * 3 +' ANÁLISIS Y RESOLUCIÓN DE ECUACIONES LINEALES')
    print('=' * 50)
    print('1. Verificar si una ecuación es lineal')
    print('2. Resolver una ecuación lineal simple (ax + b = c)')
    print('3. Resolver un sistema de dos ecuaciones lineales con dos incógnitas')
    print('4. Salir')
    print()

def display_is_linear_equation() -> None:
    """
    Interacción con el programa principal y la ejecución de la
    interactividad desde la interfaz de esta opción, la solicitud de
    datos al usuario, la impresión en pantalla de los resultados y su
    interpretación matemática.

    Objetivo:
    Mostrar la definición de ecuación lineal
    """

    print('-' * 50)
    
    result: list[str] = is_linear_equation()
    for ln in result:
        print(ln)

    print('-' * 50)
    print()

def display_solve_simple_linear_eq() -> None:
    """
    Interacción con el programa principal y la ejecución de la
    interactividad desde la interfaz de esta opción, la solicitud de
    datos al usuario, la impresión en pantalla de los resultados y su
    interpretación matemática.

    Objetivo:
    Guiar al usuario para ingresar los datos, ver el proceso y la
    interpretación matemática de una ecuación lineal simple.
    """
        
    print('-' * 50)

    print('Estructura:')
    print('\tax + b = c')

    a: float = validate_num_input('Ingrese coeficiente \'a\': ' )
    b: float = validate_num_input('Ingrese constante \'b\': ')
    c: float = validate_num_input('Ingrese constante \'c\': ')

    result: dict = solve_simple_linear_eq(a, b, c)

    print('\nProcedimiento')
    for step in result['steps']:
        print(f'>>> {step}')
    try:
        print(f'>>> x = {result['x']}')
    except KeyError:
        print('\nResultados')
        print(f'Clasificación: {result['algebraic_conclusion']}')
        print(f'Interpretación: {result['geometric_interpretation']}')
    else:
        print('\nResultados')
        print(f'Resultado final: x = {result['x']}')
        print(f'Clasificación: {result['algebraic_conclusion']}')
        print(f'Interpretación: {result['geometric_interpretation']}')

    print('-' * 50)
    print()

def display_solve_linear_system_2x2() -> None:
    """
    Interacción con el programa principal y la ejecución de la
    interactividad desde la interfaz de esta opción, la solicitud de
    datos al usuario, la impresión en pantalla de los resultados y su
    interpretación matemática.

    Objetivo:
    Guiar al usuario para ingresar los datos, ver el proceso y la
    interpretación matemática de los resultados de la solución de
    un sistema de dos ecuaciones lineales con dos incógnitas.
    """

    print('-' * 50)

    print('Estructura:')
    print('\ta₁x + b₁y = c₁')
    print('\ta₂x + b₂y = c₂')

    print('Primera ecuación (a₁x + b₁y = c₁)')

    a1: float = validate_num_input('Ingrese el coeficiente \'a₁\': ')
    b1: float = validate_num_input('Ingrese el coeficiente \'b₁\': ')
    c1: float = validate_num_input('Ingrese la constante \'c₁\': ' )

    print('\nSegunda ecuación (a₂x + b₂y = c₂)')

    a2: float = validate_num_input('Ingrese el coeficiente \'a₂\': ')
    b2: float = validate_num_input('Ingrese el coeficiente \'b₂\': ')
    c2: float = validate_num_input('Ingrese la constante \'c₂\': ' )

    result: dict = solve_linear_system_2x2(a1, b1, c1, a2, b2, c2)

    print('\nProcedimiento')
    for step in result['steps']:
        print(f'>>> {step}')
    try:
        print(f'>>> x = {result['x']}')
        print(f'>>> y = {result['y']}')
    except KeyError:
        print('\nResultados')
        print(f'Clasificación: {result['algebraic_conclusion']}')
        print(f'Interpretación: {result['geometric_interpretation']}')
    else:
        print('\nResultados')
        print(f'Resultado final: x = {result['x']}')
        print(f'Resultado final: y = {result['y']}')
        print(f'Clasificación: {result['algebraic_conclusion']}')
        print(f'Interpretación: {result['geometric_interpretation']}')

    print('-' * 50)
    print()