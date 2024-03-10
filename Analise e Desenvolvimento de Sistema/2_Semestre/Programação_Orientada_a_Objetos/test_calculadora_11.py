from calculadora_11 import Calculadora


def test_01_soma_0_0():
    calc = Calculadora()
    assert calc.soma(0, 0) == 0


def test_02_soma_0_10():
    calc = Calculadora()
    assert calc.soma(0, 10) == 10
    assert calc.soma(10, 0) == 10


def test_03_soma_6_3():
    calc = Calculadora()
    assert calc.soma(6, 3) == 9
    assert calc.soma(3, 6) == 9


def test_04_subtrai_10_2():
    calc = Calculadora()
    assert calc.subtrai(10, 2) == 8


def test_05_subtrai_2_10():
    calc = Calculadora()
    assert calc.subtrai(2, 10) == -8


def test_06_subtrai_10_0():
    calc = Calculadora()
    assert calc.subtrai(10, 0) == 10


def test_07_subtrai_0_0():
    calc = Calculadora()
    assert calc.subtrai(0, 0) == 0
