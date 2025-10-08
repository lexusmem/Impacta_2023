import unittest


def soma(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        raise TypeError(f'Tipos incompatíveis')


class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 5), 5)

    def test_soma_negativo_positivo(self):
        self.assertEqual(soma(-3, 5), 2)

    def test_soma_tipo_string(self):
        with self.assertRaises(TypeError):
            soma(2, "3")
        with self.assertRaises(TypeError):
            soma("2", 3)

    def test_excecao_tipos_float(self):
        self.assertRaises(TypeError, soma, 2.5, 3.5)
        self.assertRaises(TypeError, soma, 5, 3.5)
        self.assertRaises(TypeError, soma, 5.5, 3)

    def test_exececao_tipos_boolean(self):
        self.assertRaises(TypeError, soma, True, False)
        self.assertRaises(TypeError, soma, False, True)
        self.assertRaises(TypeError, soma, 1, True)
        self.assertRaises(TypeError, soma, False, 1)


if __name__ == '__main__':
    unittest.main()
