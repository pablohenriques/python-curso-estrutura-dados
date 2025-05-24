from dis import pretty_flags


class No:

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostrar_no(self):
        print(self.valor)


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def inserir(self, valor):
        novo = No(valor)

        # se a arvore estiver vazia
        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz

            while True:
                pai = atual

                # esquerda
                if valor < atual.valor:
                    atual = atual.esquerda

                    if atual is None:
                        pai.esquerda = novo
                        self.ligacoes.append(str(pai.valor) +'->'+ str(novo.valor))
                        break

                # direita
                else:
                    atual = atual.direita

                    if atual is None:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        break

    def pesquisar(self, valor):
        atual = self.raiz

        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

            if atual is None:
                break
        return atual

if __name__ == '__main__':
    arvore = ArvoreBinariaBusca()
    arvore.inserir(53)
    arvore.inserir(30)
    arvore.inserir(14)
    arvore.inserir(39)
    arvore.inserir(9)
    arvore.inserir(23)
    arvore.inserir(34)
    arvore.inserir(49)
    arvore.inserir(72)
    arvore.inserir(61)
    arvore.inserir(84)
    arvore.inserir(79)
    print(arvore.raiz.esquerda.valor)
    print(arvore.raiz.direita.valor)
    print(arvore.ligacoes)
    print(arvore.pesquisar(23).valor)