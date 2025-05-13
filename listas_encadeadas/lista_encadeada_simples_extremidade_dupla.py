class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeadaExtremidadeDupla:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.ultimo = novo

        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo

        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('Lista está vazia')

        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp

    def mostrar(self):
        if self.__lista_vazia():
            print('Lista vazia')
            return

        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo


if __name__ == '__main__':
    lista = ListaEncadeadaExtremidadeDupla()

    # insere no inicio e mostra
    # lista.insere_inicio(1)
    # lista.mostrar()
    # print(f'primeiro lista: {lista.primeiro} - segundo lista: {lista.ultimo}')
    # lista.insere_inicio(2)
    # lista.insere_inicio(3)
    # lista.insere_inicio(4)
    # lista.insere_inicio(5)
    # lista.mostrar()
    # print(f'primeiro lista: {lista.primeiro} - segundo lista: {lista.ultimo}')

    # insere no final
    # lista.insere_final(9)
    # print(f'primeiro lista: {lista.primeiro} - segundo lista: {lista.ultimo}')
    # lista.insere_final(8)
    # lista.insere_final(7)
    #
    # lista.mostrar()
    #
    # lista.insere_inicio(0)
    # lista.insere_final(4)
    #
    # lista.mostrar()

    # excluir inicio

    lista.insere_inicio(1)
    lista.insere_final(3)
    lista.mostrar()
    lista.excluir_inicio()
    lista.mostrar()
    lista.excluir_inicio()
    lista.mostrar()
