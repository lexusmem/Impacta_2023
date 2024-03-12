def incrementa_int(n):
    print('Função incrementa_int: n =', n)
    if not isinstance(n, int):
        raise TypeError('O número deve ser inteiro.')
    return n + 1


def calcula_idade(idade):
    nova_idade = incrementa_int(idade)
    print('Esse código não é executado se der erro na função incrementa_int.')
    return nova_idade


def main():
    print('Executando a função principal...')
    resposta = calcula_idade(20)
    print('Esse código não será executado se der erro na função incrementa_int.')
    print('A nova idade é:', resposta)


if __name__ == '__main__':
    print('Chamando a função main()')
    main()
    print('Não será executado se existir erro na função incrementa_int.')
