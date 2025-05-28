from dis import pretty_flags
from os import supports_effective_ids


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

    # raiz, esquerda, direita
    def pre_ordem(self, no):
        if no is not None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    # raiz, esquerda, direita
    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    # esquerda, direita, raiz
    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def excluir(self, valor):
        if self.raiz is None:
            print('A árvore está vazia')
            return None

        # encontrar o no
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True

        while atual.valor is not valor:
            pai = atual

            # esquerda
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            # direita
            else:
                e_esquerda = False
                atual = atual.direita

            if atual is None:
                return False

        # o no a ser apagado eh uma folha
        if atual.esquerda is None and atual.direita is None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda is True:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
                pai.esquerda = None
            else:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
                pai.direita = None

        # o no nao possui filho na direita
        elif atual.direita is None:
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.esquerda.valor))

            if atual == self.raiz:
                self.raiz = atual.esquerda
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(atual.esquerda.valor))
            elif e_esquerda is True:
                pai.esquerda = atual.esquerda
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.esquerda.valor))
            else:
                pai.direita = atual.esquerda
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.esquerda.valor))

        # o no nao possui filho na esquerda
        elif atual.esquerda is None:
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.direita.valor))

            if atual == self.raiz:
                self.raiz = atual.direita
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(atual.direita.valor))
            elif e_esquerda is True:
                pai.esquerda = atual.direita
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.direita.valor))
            else:
                pai.direita = atual.direita
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.direita.valor))

        # no possui dois filhos
        else:
            sucessor = self.get_sucessor(atual)

            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.direita.valor) + '->' + str(sucessor.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.esquerda.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.direita.valor))

            if atual == self.raiz:
                self.raiz = sucessor
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(sucessor.valor))
            elif e_esquerda is True:
                pai.esquerda = sucessor
                self.ligacoes.append(str(pai.valor) + '->' + str(sucessor.valor))
            else:
                pai.direita = sucessor
                self.ligacoes.append(str(pai.valor) + '->' + str(sucessor.valor))

            self.ligacoes.append(str(sucessor.valor) + '->' + str(atual.esquerda.valor))
            self.ligacoes.append(str(sucessor.valor) + '->' + str(atual.direita.valor))

            sucessor.esquerda = atual.esquerda

        return True

    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita

        while atual is not None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        return sucessor



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
    #print(arvore.raiz.esquerda.valor)
    # print(arvore.raiz.direita.valor)
    # print(arvore.ligacoes)
    # print(arvore.pesquisar(23).valor)

    # print(arvore.pre_ordem(arvore.raiz))
    # print(arvore.em_ordem(arvore.raiz))
    # print(arvore.pos_ordem(arvore.raiz))
    # arvore.excluir(9)
    # print(arvore.ligacoes)
    # arvore.excluir(79)
    # print(arvore.ligacoes)

    # print(arvore.ligacoes)
    # arvore.excluir(84)
    # print(arvore.ligacoes)
    #
    # arvore.excluir(9)
    # arvore.excluir(14)
    # print(arvore.ligacoes)
    # print(arvore.get_sucessor(arvore.raiz).valor)

    arvore.excluir(72)
    print(arvore.ligacoes)
    arvore.excluir(30)
    print(arvore.ligacoes)
