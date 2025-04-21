# Big O -> O(n)
def lista_simples():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

# Big O -> criacao: O(1)
# Big O -> iteracao: O(n)
def lista_range():
    return range(1000)


if __name__ == '__main__':
    print(lista_simples())
    print(lista_range())
    print([i for i in lista_range()])
