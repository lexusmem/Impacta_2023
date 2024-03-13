def incrementa_int(n):
    print('Função incrementa_int: n =', n)
    if not isinstance(n, int):
        raise TypeError
    return n + 1


def calcula_idade(idade):
    try:
        nova_idade = incrementa_int(idade)
    except TypeError:
        print('O número deve ser inteiro.')
        raise
    except Exception:
        print('Deu Erro!')
        raise
    else:
        print(
            'A função calcula_idade não é executado se der erro na função incrementa_int.')
        return nova_idade


def main():
    print('Executando a função principal...')
    try:
        resposta = calcula_idade(20.5)
    except Exception:
        print('Tente novamente....')
    else:
        print('A função main não será executado se der erro na função incrementa_int.')
        print('A nova idade é:', resposta)


if __name__ == '__main__':
    print('Chamando a função main()')
    main()
    print('Não deu erro no nosso programa, os erros ocorridos foram tratados.')
