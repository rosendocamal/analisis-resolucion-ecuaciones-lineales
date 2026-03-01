# Análisis y Resolución de Ecuaciones y Sistemas Lineales en Python

## Resumen

Proyecto Integrador donde se aplican los conocimientos básicos de Álgebra Lineal y de programación en el lenguaje de Python. Con el propósito de mostrar la comprensión de conceptos matemáticos que pueden representarse, validarse y resolverse mediante un algoritmo estruturado.

Es un programa realizado 100% en Python que permite resolver ecuaciones lineales simples de la forma `ax + b = c` y sistemas de dos ecuaciones lineales con dos incógnitas de la forma `a₁x + b₁y = c₁` con `a₂x + b₂y = c₂`. Con la particularidad de que arroja los resultados en caso de ser posibles (no hay contradicciones ni divisiones entre cero) con la interpretación tanto geométrica como la algebraica en ambos casos. Es decir, muestra el procedimiento matemático y la interpretación del resultado.

A través de la **CLI** el programa permite una interactividad fluida a través de las opciones que ofrece.

## Estructura del Proyecto

El código ha sido organizado de la siguiente manera:

* `main.py`: Es el archivo principal en donde se vincula los archivos `cli.py` y `testing.py` con el objetivo de que permita ejecutar el menú interactivo después de que se hayan ejecutado las pruebas.
    * `src/solver/`:
        * `cli.py`: Interfaz de la línea de comandos y el flujo interactivo del menú.
        * `math.py`: Funciones matemáticas.
        * `testing.py`: Sistema de prueba implementado con `asserts`.
        * `validates.py`: Filtros para validar las entradas númericas solicitadas al usuario.

## Requisitos y Tecnologías

* **Python 3.10 o superior** (debido al uso de `match-case` para el menú).
* No requiere librerías externas (**Standard Libray** únicamente).
* Se ha desarrollado en un entorno Linux usando el sistema operativo `Fedora 43`, acompañado de herramientas y servicios como `git`, `nvim`, `GitHub` y `Visual Studio Code`.

## Validación de entrada y testing

Antes de iniciar la interfaz del menú, el archivo `main.py` ejecuta automáticamente una serie de **pruebas** predefinidos en `testing.py` mediante la palabra reservada de Python `assert`.

En el archivo `testing.py` se encuentra las siguientes pruebas:

1. `Determinante`: Se prueba usando un los valores de una matriz 2x2.
2. `Sistema Lineal Simple`: Se prueba usando los tres casos posibles (**Caso normal**, **Identidad**, **Contradicción**).
3. `Sistema Lineal de 2 ecuaciones con 2 variables`: Se utiliza tres pruebas considerando los tres casos posibles de resultados matemáticos (**Intersección de rectas**, **Rectas paralelas**, **Misma recta**).

> **Nota**: Si alguna de estas pruebas falla, el programa no ejecuta para garantizar la calidad de los resultados matemáticos.

## Instrucciones de uso

1. Clona el repositorio. Para ello, ejecuta el siguiente comando:
```
git clone https://github.com/rosendocamal/analisis-resolucion-ecuaciones-lineales.git
```

2. Ubícate en la carpeta principal del repositorio y ejecuta:
```
python3 main.py
```

3. Sigue las intrucciones del menú interactivo.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles consulta el archivo [LICENSE](LICENSE).

## Autor

Proyecto desarrollado por **Rosendo Camal**.

Contacto:
* [`GitHub`](https://github.com/rosendocamal)
* [`Linkedin`](https://www.linkedin.com/in/rosendocamal)