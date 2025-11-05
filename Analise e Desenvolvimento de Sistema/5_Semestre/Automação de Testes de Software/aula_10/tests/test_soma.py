"""Soma feature tests."""
from pytest import fixture
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from app.soma import soma


@fixture
def context():
    return {'num1': 0, 'num2': 0, 'resultado': 0}


@scenario('soma.feature', 'Soma dois numeros')
def test_soma_dois_numeros():
    """Soma dois numeros."""


@given('Tenho o primeiro valor 10 como entrada')
def tenho_primeiro_valor(context):
    """Tenho o primeiro valor 10 como entrada."""
    context['num1'] = 10


@given('Tenho o segundo valor 10 como entrada')
def tenho_segundo_valor(context):
    """Tenho o segundo valor 10 como entrada."""
    context['num2'] = 10


@when('Solicito a realização da soma')
def solicito_realizacao_soma(context):
    """Solicito a realização da soma."""
    context['resultado'] = soma(context['num1'], context['num2'])


@then('O resultado deve ser 20')
def o_resultado_deve_ser_20(context):
    """O resultado deve ser 20."""
    assert context['resultado'] == 20
