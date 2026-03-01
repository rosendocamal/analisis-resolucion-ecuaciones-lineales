# Funciones matemáticas del programa

def is_linear_equation() -> list[str]:
    """
    Guarda la definición de ecuación lineal
    en una lista para ser fácilmente impreso
    en pantalla
    
    Retorna:
    Una lista con oraciones de la definición de
    ecuación lineal
    """
    linear_equation: list[str] = [
        'Ecuación lineal',
        'Es una ecuación con variables y coeficientes',
        'Forma general: a₁x₁ + a₂x₂ + ⋯ + aₙxₙ + b = 0',
        'Donde:',
        '- x₁, …, xₙ son las variables',
        '- a₁, …, aₙ y b son números reales',
        '- al menos un coeficiente distinto de cero',
        '- cada variable aparece con exponente 1',
        '- no hay productos ni funciones no lineales',
        'Propiedades:',
        '1. El grado de la ecuación es 1',
        '2. Caso simple (n=1): ax + b = 0',
        '   Si a ≠ 0, la solución es x = -b/a'
    ] 
    
    return linear_equation

def determinant(a: float, b: float, c: float, d: float) -> float:
    """
    Calcula el determinante de una matriz de 2x2 en la
    forma de ((a, b), (c, d))
    
    Parámetros:
    a (float): Valor del primer elemento en primera fila.
    b (float): Valor del segundo elemento en primera fila.
    c (float): Valor del primer elemento en segunda fila.
    d (float): Valor del segundo elemento en segunda fila.
    
    Retorna:
    det (float): El valor del determinante de la matriz."""
    det: float = (a * d) - (b * c)
    return det

def solve_simple_linear_eq(a: float, b: float, c: float) -> dict:
    """
    Solucionador de ecuaciones lineales simples de la forma
    ax + b = c.
    
    Parámetros:
    a (float): Coeficiente de la variable única de la ecuación.
    b (float): Segundo término de la ecuación del primer miembro.
    c (float): Término del lado del segundo miembro de la ecuación.
    
    Retorna:
    result (dict): Un diccionario con los valores ingresados, con
                los pasos realizados para la solución, la interpretación
                geométrica y algebraica. Siendo accesibles mediante los
                valores de a, b, c, steps, algebraic_conclusion y
                geometric_interpretation. Solo en caso normal, se puede
                acceder al valor de x.
    """
    result: dict = {
        'a': a,
        'b': b,
        'c': c,
        'steps': [
            f'{a}x + {b} = {c}',
            f'{a}x = {c} - {b}',
            f'x = ({c} - {b}) / {a}',
            f'x = ({c - b} / {a})'
        ]
    }

    if a != 0: # Solución única (un punto en la recta númerica)
        result.update({
            'algebraic_conclusion': 'Caso normal',
            'x': (c - b) / a,
            'geometric_interpretation': 'Un único punto en la recta númerica real satisface la igualdad (solución única).'
        })
    else:
        if (c - b) == 0: # Infinitas soluciones (toda la recta númerica)
            result.update({
                'algebraic_conclusion': 'Identidad',
                'geometric_interpretation': 'Toda la recta númerica real satisface la igualdad (infinitas soluciones).'
            })
        else: # Ninguna solución (no existe ningún punto)
            result.update({
                'algebraic_conclusion': 'Contradicción',
                'geometric_interpretation': 'Ningún punto de la recta númerica real satisface la igualdad (sin solución).'
            })

    return result

def solve_linear_system_2x2(a1: float, b1: float, c1: float,
                            a2: float, b2: float, c2: float) -> dict:
    """
    Solucionador de sistemas de dos ecuaciones lineales con dos incógnitas.
    
    Parámetros:
    a1, a2 (float): Valores de la primera variable de la primera y segunda ecuación, respectivamente.
    b1, b2 (float): Valores de la segunda variable de la primera y segunda ecuación, respectivamente.
    c1, c2 (float): Valores de la constante de la primera y segunda ecuación, respectivamente.
    
    Retorna:
    result (dict): Un diccionario con los valores de los determinates
                principales, de la primera y segunda variable, los pasos
                de solución, la interpretación algebraica y geométrica de
                los resultados.
    """     
    
    det_s: float = determinant(a1, b1, a2, b2)
    det_x: float = determinant(c1, b1, c2, b2)
    det_y: float = determinant(a1, c1, a2, c2)

    result: dict = {
        'det_s': det_s,
        'det_x': det_x,
        'det_y': det_y,
        'steps': [
            f'det_s = ({a1} * {b2}) - ({b1} * {a2}) = {det_s}',
            f'det_x = ({c1} * {b2}) - ({b1} * {c2}) = {det_x}',
            f'det_y = ({a1} * {c2}) - ({c1} * {a2}) = {det_y}'
        ]
    }

    if det_s != 0: # Solución única (intersección de rectas)
        result.update({
            'algebraic_conclusion': 'Sistema compatible determinado',
            'x': det_x / det_s,
            'y': det_y / det_s,
            'geometric_interpretation': 'Las dos ecuaciones representan dos rectas que se cortan en un solo punto (solución única del sistema).'
        })
    else: 
        if det_x == 0 and det_y == 0: # Soluciones infinitas (misma recta)
            result.update({
                'algebraic_conclusion': 'Sistema compatible indeterminado',
                'geometric_interpretation': 'Las dos ecuaciones representan la misma recta (hay infinitas soluciones).'
            })
        else: # Sin solución (rectas paralelas)
            result.update({
                'algebraic_conclusion': 'Sistema incompatible',
                'geometric_interpretation': 'Las dos ecuaciones representan dos rectas paralelas que nunca se cortan (sin solución).'
            })
    return result