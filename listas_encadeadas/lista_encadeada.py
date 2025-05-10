import numpy as np


class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeada:

    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostar(self):
        if self.primeiro == None:
            print('Lista está vazia')
            return None

        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def excluir_inicio(self):
        if self.primeiro is None:
            print('Lista está vazia')
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def pesquisa(self, valor):
        if self.primeiro is None:
            print('Lista está vazia')
            return None

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo is None:
                return None
            else:
                atual = atual.proximo
        return atual

    def excluir_posicao(self, valor):
        if self.primeiro is None:
            print('Lista está vazia')
            return None

        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo is None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual







if __name__ == '__main__':
    lista = ListaEncadeada()
    lista.insere_inicio(1)
    lista.insere_inicio(2)
    lista.insere_inicio(3)
    #lista.mostar()
    print('-------------')
    #lista.excluir_inicio()
    #lista.excluir_inicio()
    lista.mostar()
    #p = lista.pesquisa(3)
    #print(p, p.valor)
    print('-------------')
    lista.excluir_posicao(2)
    lista.mostar()