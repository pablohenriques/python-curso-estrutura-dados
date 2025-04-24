import numpy as np


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for indice in range(self.ultima_posicao + 1):
                print(f'Índice: {indice} - Valor: {self.valores[indice]}')

    # O(n)
    def inserir(self, valor):
        if self.ultima_posicao == (self.capacidade -1):
            print('Capacidade máxima atingida')
        else:
            posicao = 0
            for indice in range(self.ultima_posicao + 1):
                posicao = indice
                if self.valores[indice] > valor:
                    break

                if indice == self.ultima_posicao:
                    posicao = indice + 1

            ponteiro = self.ultima_posicao
            while ponteiro >= posicao:
                self.valores[ponteiro + 1] = self.valores[ponteiro]
                ponteiro -= 1

            self.valores[posicao] = valor
            self.ultima_posicao += 1

    def pesquisar(self, valor):
        resultado = None
        for indice in range(self.ultima_posicao + 1):
            if self.valores[indice] > valor:
                resultado = -1
                break
            if self.valores[indice] == valor:
                resultado = indice
                break
            if indice == self.ultima_posicao:
                resultado = -1
                break
        return resultado


    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior)/2)

            # de primeira
            if self.valores[posicao_atual] == valor:
                return posicao_atual

            # não encontrou
            elif limite_inferior > limite_superior:
                return -1

            # Divide os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1


    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            return None


if __name__ == '__main__':
    vetor = VetorOrdenado(5)

    vetor.inserir(3)
    vetor.inserir(4)
    vetor.inserir(5)
    vetor.inserir(6)
    vetor.inserir(7)

    vetor.imprimir()

    print(vetor.pesquisa_binaria(5))
    print(vetor.pesquisa_binaria(3))
    print(vetor.pesquisa_binaria(6))
    print(vetor.pesquisa_binaria(9))
