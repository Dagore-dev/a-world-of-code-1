# **Ejercicio 01.13** Área de un triángulo a partir de sus puntos:
# 1) Escribir una función que dado un vector al origen (definido por sus puntos `x`, `y`),
# devuelva la norma del vector, dada por `(x^2 + y^2) ^ 1/2`
# 2) Escribir una función que dados dos puntos en el plano (`x1`, `y1` y `x2`, `y2`), devuelva la resta de ambos
# (debe devolver un par de valores).
#
# 3) Utilizando las funciones anteriores, escribir una función que dados dos puntos en el plano
# (`x1`, `y1` y`x2`, `y2`), devuelva la distancia entre ambos.
#
# 4) Escribir una función que reciba un vector al origen (definido por sus puntos `x`, `y`) y
# devuelva un vector equivalente, normalizado (debe devolver un par de valores).
#
# 5) Utilizando las funciones anteriores (`b` y `d`), escribir una función que dados dos puntos en el plano
# (`x1`, `y1` y `x2`, `y2`), devuelva el vector dirección unitario correspondiente a la recta que los une.
#
# 6) Escribir una función que reciba un punto `(x, y)`, una dirección unitaria de una recta `(dx, dy)` y
# un punto perteneciente a esa recta `(cx, cy)` y devuelva la proyección del punto sobre la recta.
#
# **Diseño del algoritmo:**
#
# 1. Al punto a proyectar `(x, y)` restarle el punto de la recta `(cx, cy)`
# 2. Obtener la matriz de proyección `P`, dada por: `p11 = dx^2`, `p12 = p21 = dx * dy`, `p22 = dy^2`.
# 3. Multiplicar la matriz `P` por el punto obtenido en el paso 1: `rx = p11 * x + p12 * y`, `ry = p21 * x + p22 * y`.
# 4. Al resultado obtenido sumar el punto restado en el paso 1, y devolverlo.
#
# 7) Escribir una función que calcule el área de un triángulo a partir de su base y su altura.
#
# 8) Utilizando las funciones anteriores escribir una función que reciba tres puntos en el plano
# (`x1`, `y1`,`x2`, `y2` y `x3`, `y3`) y devuelva el área del triángulo correspondiente.
import math


def get_vector_norm(x: int, y: int) -> float:
    """
    Get the norm of the given vector defined by x and y as a float number
    :param x: Integer representing a point of a vector
    :param y: Integer representing a point of a vector
    :return: Norm of given vector given by (x^2 + y^2) ^ 1/2

    >>> get_vector_norm(0, 2)
    2.0
    """
    return math.sqrt((x**2 + y**2))


def sum_vectors(v1: (int, int), v2: (int, int)) -> (int, int):
    """
    Sum two vectors
    :param v1: A tuple of two integers representing a simple vector
    :param v2: A tuple of two integers representing a simple vector
    :return: A tuple with the sum vector

    >>> sum_vectors((8, 13), (26, 7))
    (34, 20)
    """
    return v1[0] + v2[0], v1[1] + v2[1]


def subtract_vectors(v1: (int, int), v2: (int, int)) -> (int, int):
    """
    Substract two vectors
    :param v1: A tuple of two integers representing a simple vector
    :param v2: A tuple of two integers representing a simple vector
    :return: A tuple with the subtract vector

    >>> subtract_vectors((4, 5), (12, 2))
    (-8, 3)
    """
    return sum_vectors(v1, (-v2[0], -v2[1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
