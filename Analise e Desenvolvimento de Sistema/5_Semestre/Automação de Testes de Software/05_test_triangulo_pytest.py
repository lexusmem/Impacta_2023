import pytest
from pytest_triangulo import triangulo


def test_triangulo_escaleno():
    assert triangulo(2, 5, 4) == "Escaleno"


def test_triangulo_isosceles():
    assert triangulo(4, 5, 4) == "Isósceles"


def test_triangulo_equilatero():
    assert triangulo(3, 3, 3) == "Equilátero"


def test_triangulo_nao_triangulo():
    assert triangulo(0, 4, 4) == "Inválido"


def test_triangulo_float_int():
    with pytest.raises(TypeError):
        triangulo(2, 4, '4')
