from dirigir import dirigir


def test_pode_dirigir():
    assert dirigir(18, 's') == "Pode dirigir"


def test_não_pode_dirigir():
    assert dirigir(17, 's') == "Não Pode dirigir"


def test_não_pode_dirigir_habilitacao():
    assert dirigir(30, 'n') == "Não Pode dirigir"
