def constant(elementos):
    print(elementos[0])


def linear(elementos):
    for item in elementos:
        print(item, end="")
    print("")


def quadratic(elementos):
    for linha in elementos:
        for coluna in elementos:
            print(linha, coluna, end="")
        print("|")

# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n)
# O(n)
def combination(elementos):
    # O(1)
    print(elementos[0])

    # O(5)
    for i in range(5):
        print('test', i)

    # O(n)
    for item in elementos:
        print(item)

    # O(n)
    for item in elementos:
        print(item)

    # O(3)
    print('Python')
    print('Python')
    print('Python')


if __name__ == '__main__':
    lista = range(1, 6)
    # constant(lista)
    # linear(lista)
    # quadratic(lista)
    combination(lista)
