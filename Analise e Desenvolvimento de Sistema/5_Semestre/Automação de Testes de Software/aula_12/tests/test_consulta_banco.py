"""Aplicação web para banco feature tests."""

import pytest

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def navegador():
    opts = Options()
    opts.headless = True
    servico = Service(ChromeDriverManager().install())
    chrome = Chrome(service=servico, options=opts)
    yield chrome
    chrome.quit()


@scenario('features/banco.feature', 'Obter o saldo da conta')
def test_obter_o_saldo_da_conta(navegador):
    """Obter o saldo da conta."""


@given('eu visito o app do banco')
def eu_visito_o_app_do_banco(navegador):
    """eu visito o app do banco."""
    navegador.get('http://127.0.0.1:5000/nova_conta')
    form = navegador.find_element(By.ID, "form_conta")
    num_conta = navegador.find_element(By.ID, "numero")
    num_conta.send_keys("111")
    saldo = navegador.find_element(By.ID, "saldo")
    saldo.send_keys("50")
    form.submit()


@when('eu entro com o número da conta "111"')
def eu_entro_com_o_número_da_conta_1111(navegador):
    """eu entro com o número da conta "1111"."""
    navegador.get('http://127.0.0.1:5000/consulta')
    form = navegador.find_element(By.ID, "form_consulta_conta")
    num_conta = navegador.find_element(By.NAME, "numero_conta")
    num_conta.send_keys("111")
    form.submit()


@then('eu obtenho saldo igual a 50')
def eu_obtenho_saldo_igual_a_50(navegador):
    """eu obtenho saldo igual a 50."""
    result = navegador.find_element(By.TAG_NAME, 'p')
    assert result.text == 'Saldo: 50'


"""Aplicação web para banco feature tests."""


@pytest.fixture
def navegador():
    opts = Options()
    opts.headless = True
    servico = Service(ChromeDriverManager().install())
    chrome = Chrome(service=servico, options=opts)
    yield chrome
    chrome.quit()


@scenario('features/banco.feature', 'Obter o saldo da conta')
def test_obter_o_saldo_da_conta(navegador):
    """Obter o saldo da conta."""


@given('eu visito o app do banco')
def eu_visito_o_app_do_banco(navegador):
    """eu visito o app do banco."""
    navegador.get('http://127.0.0.1:5000/nova_conta')
    form = navegador.find_element(By.ID, "form_conta")
    num_conta = navegador.find_element(By.ID, "numero")
    num_conta.send_keys("111")
    saldo = navegador.find_element(By.ID, "saldo")
    saldo.send_keys("50")
    form.submit()


@when('eu entro com o número da conta "111"')
def eu_entro_com_o_número_da_conta_1111(navegador):
    """eu entro com o número da conta "1111"."""
    navegador.get('http://127.0.0.1:5000/consulta')
    form = navegador.find_element(By.ID, "form_consulta_conta")
    num_conta = navegador.find_element(By.NAME, "numero_conta")
    num_conta.send_keys("111")
    form.submit()


@then('eu obtenho saldo igual a 50')
def eu_obtenho_saldo_igual_a_50(navegador):
    """eu obtenho saldo igual a 50."""
    result = navegador.find_element(By.TAG_NAME, 'p')
    assert result.text == 'Saldo: 50'
