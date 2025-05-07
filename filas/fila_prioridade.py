import numpy as np


class FilaPrioridade:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos-1]

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila está cheia')
            return

        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            indice = self.numero_elementos - 1

            while indice >= 0:
                if valor > self.valores[indice]:
                    self.valores[indice+1] = self.valores[indice]
                else:
                    break
                indice -= 1
            self.valores[indice + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return
        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor


if __name__ == '__main__':
    fila = FilaPrioridade(5)
    print(fila.primeiro())

    fila.enfileirar(30)
    print(fila.primeiro())

    fila.enfileirar(50)
    print(fila.primeiro())

    fila.enfileirar(10)
    print(fila.primeiro())

    print(fila.valores)

    fila.enfileirar(40)
    print(fila.primeiro())

    print(fila.valores)

    fila.enfileirar(2)
    print(fila.primeiro())

    print(fila.valores)

    print(fila.desenfileirar())
    print(fila.primeiro())

    print(fila.valores)


    print(fila.desenfileirar())
    print(fila.primeiro())

    print(fila.valores)

    print(fila.enfileirar(5))
    print(fila.primeiro())

    print(fila.valores)