# Evaluación de las funciones matemáticas del programa

from .math import determinant, solve_simple_linear_eq, solve_linear_system_2x2

def test_determinant() -> None:
    """
    Test para evaluar la función del determinante
    """
    result: float = determinant(5, 4, 2, 3)

    assert result == 7

def test_solve_simple_linear_eq() -> None:
    """
    Test para evaluar la función de la resolución de
    ecuaciones lineales simples
    """

    # Primera prueba: ax + b = c
    result_normal: dict = solve_simple_linear_eq(2, 3, 5)

    assert result_normal['x'], 2 == 1
    assert result_normal['algebraic_conclusion'] == 'Caso normal'

    # Segunda prueba: 0 = 0
    result_identidad: dict = solve_simple_linear_eq(0, 0, 0)

    assert result_identidad['algebraic_conclusion'] == 'Identidad'

    # Tercera prueba: b = c cuando  b <> c
    result_contradiccion: dict = solve_simple_linear_eq(0, -3, 9)

    assert result_contradiccion['algebraic_conclusion'] == 'Contradicción'

def test_solve_linear_system_2x2() -> None:
    """
    Test para evaluar la función de la resolución
    de sistemas de dos ecuaciones de dos incógnitas"""
    # Primera prueba
    result_scd: dict = solve_linear_system_2x2(1, 1, 2, 1, -1, 0)

    assert result_scd['x'] == 1
    assert result_scd['y'] == 1
    assert result_scd['algebraic_conclusion'] == 'Sistema compatible determinado'

    # Segunda prueba
    result_sci: dict = solve_linear_system_2x2(1, 1, 5, 2, 2, 10)

    assert result_sci['algebraic_conclusion'] == 'Sistema compatible indeterminado'

    # Tercera prueba
    result_si: dict = solve_linear_system_2x2(1, 1, 5, 1, 1, 10)

    assert result_si['algebraic_conclusion'] == 'Sistema incompatible'

def run_test() -> None:
    """
    Función que encapsula las pruebas de test
    """
    test_determinant()
    test_solve_simple_linear_eq()
    test_solve_linear_system_2x2()