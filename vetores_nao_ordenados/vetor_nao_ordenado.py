import numpy as np


class VetorNaoOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for indice in range(self.ultima_posicao + 1):
                print(f'{indice} - {self.valores[indice]}')

    # O(2)
    def insere(self, valor):
        if self.ultima_posicao == (self.capacidade - 1):
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O(n)
    def pesquisar(self, valor):
        for indice in range(self.ultima_posicao + 1):
            if valor == self.valores[indice]:
                return indice
        return -1

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            self.ultima_posicao -= 1
            return None


if __name__ == '__main__':
    vetor = VetorNaoOrdenado(5)
    vetor.imprime()
    vetor.insere(3)
    vetor.insere(5)
    vetor.insere(8)
    vetor.insere(1)
    vetor.insere(0)
    vetor.imprime()
    vetor.insere(7)
    print(vetor.pesquisar(8))
    print("--")
    vetor.excluir(5)
    vetor.imprime()
    print("--")
    vetor.excluir(1)
    vetor.imprime()
