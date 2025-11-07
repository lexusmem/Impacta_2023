Feature: Aplicação web para banco
    Obter e atualizar contas de clientes

    Como um cliente eu quero ser capaz de vizualizar o meu saldo
    e atualizar o saldo
    e sacar um valor do saldo

Scenario: Obter o saldo da conta
    Given eu visito o app do banco
    When eu entro com o número da conta "111"
    Then eu obtenho saldo igual a 50