from ...soma import soma
from behave import given, when, then


@given('Primeiro valor sera 5')
def given_primeiro_valor(context):
    context.num1 = 5


@given('Segundo valor sera 2')
def given_segundo_valor(context):
    context.num2 = 2


@when('Executa a funcao')
def when_executa_funcao(context):
    context.saida = soma(context.num1, context.num2)


@then('Saida deve ser o valor 7')
def then_saida_deve_ser_7(context):
    assert context.saida == 7
