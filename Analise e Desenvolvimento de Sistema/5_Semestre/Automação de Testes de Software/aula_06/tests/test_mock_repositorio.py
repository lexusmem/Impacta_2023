import pytest
from datetime import date
from unittest.mock import Mock
from src.livro import Livro


@pytest.fixture
def livro():
    l1 = Livro('111', 'python para iniciantes', 50.0, date.today())
    return l1


def test_busca_livro_por_id(livro):
    livroRepositorio = Mock()
    livroRepositorio.obter_livro.return_value = livro
    livroRepositorio.numero_de_chamadas.return_value = 2
    resultado = livroRepositorio.obter_livro('111')
    resultado = livroRepositorio.obter_livro('222')

    assert resultado.id == '111'
    assert resultado.titulo == 'python para iniciantes'
    assert livroRepositorio.numero_de_chamadas() == 1
    livroRepositorio.obter_livro.assert_called_once()
    livroRepositorio.obter_livro.assert_called_once_with('111')
