from grafos.fila_circular_grafo import FilaCircularGrafo
from grafos.pilha_grafo import PilhaGrafo
from grafos.vetor_grafo import VetorOrdenado
from grafos.vetor_ordenado_grafos import VetorOrdenadoEstrela


class BuscaProfundidade:

    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.pilha = PilhaGrafo(20)
        self.pilha.empilhar(inicio)

    def buscar(self):
        topo = self.pilha.ver_topo()
        print(f'Topo: {topo.rotulo}')
        for adjacente in topo.adjacentes:
            print(f'Topo é {topo.rotulo}. {adjacente.vertice.rotulo} já foi visitada? {adjacente.vertice.visitado}')
            if adjacente.vertice.visitado is False:
                adjacente.vertice.visitado = True
                self.pilha.empilhar(adjacente.vertice)
                print(f'Empilhou {adjacente.vertice.rotulo}')
                self.buscar()
        print(f'Desempilhou: {self.pilha.desempilhar().rotulo}\n')


class BuscaLargura:

    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.fila = FilaCircularGrafo(20)
        self.fila.enfileirar(inicio)

    def buscar(self):
        primeiro = self.fila.primeiro()
        print('-----------')
        print(f'Primeiro Fila: {self.fila.primeiro().rotulo}')

        temp = self.fila.desenfileirar()
        print(f'Desenfileirou: {temp.rotulo}')

        for adjacente in primeiro.adjacentes:
            print('Primeiro era {}. {} já foi visitado ? {}'.format(
                temp.rotulo,
                adjacente.vertice.rotulo,
                adjacente.vertice.visitado
            ))

            if adjacente.vertice.visitado is False:
                adjacente.vertice.visitado = True
                self.fila.enfileirar(adjacente.vertice)
                print(f'Enfileirou {adjacente.vertice.rotulo}')

        if self.fila.numero_elementos > 0:
            self.buscar()


class BuscaGulosa:

    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('----------')
        print(f'Atual: {atual.rotulo}')
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado is False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente.vertice)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0])


class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('----------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenadoEstrela(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado is False:
          adjacente.vertice.visitado = True
          vetor_ordenado.insere(adjacente)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] is not None:
        self.buscar(vetor_ordenado.valores[0].vertice)