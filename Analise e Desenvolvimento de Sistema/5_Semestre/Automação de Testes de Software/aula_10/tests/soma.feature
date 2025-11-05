Feature: Soma
    a função recebe dois valores e retorna a soma dos valores.

Scenario: Soma dois numeros
    Given Tenho o primeiro valor 10 como entrada
    And Tenho o segundo valor 10 como entrada
    When Solicito a realização da soma
    Then O resultado deve ser 20
