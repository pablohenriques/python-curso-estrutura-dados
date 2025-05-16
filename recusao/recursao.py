def recursao(parada):
    print('Recursão DEF')

    parada += 1
    if parada == 5:
        return 0
    else:
        return recursao(parada)


def soma_for(n):
    return sum(x for x in range(n + 1))


def soma_recursao(n):
    if n == 0:
        return 0

    return n + soma_recursao(n - 1)


def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n-1)


def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)


if __name__ == '__main__':
    # for _ in range(5):
    #     print('Recursão FOR')

    recursao(0)
    print(f'Soma FOR: {soma_for(2)}')
    print(f'Soma RECURSÃO: {soma_recursao(2)}')
    print(f'Fatorial: {fatorial(5)}')
    print(f'Potência: {potencia(2, 4)}')
