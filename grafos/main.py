from grafos.busca import BuscaLargura, BuscaGulosa, AEstrela
from grafos.fila_circular_grafo import FilaCircularGrafo
from grafos.grafo import GrafoG, Grafo, GrafoA
from grafos.vetor_grafo import VetorOrdenado

if __name__ == '__main__':
    grafo = GrafoA()
    # grafo = GrafoG()
    # grafo = Grafo()
    # fila = FilaCircularGrafo(20)
    # grafo.bucharest.mostrar_adjacentes()

    # pilha = PilhaGrafo(5)
    # pilha.empilhar(grafo.arad)
    # pilha.empilhar(grafo.sibiu)
    # pilha.empilhar(grafo.timisoara)
    # print(pilha.desempilhar().rotulo)
    # print(pilha.desempilhar().rotulo)

    # busca_profundidade = BuscaProfundidade(grafo.arad)
    # busca_profundidade.buscar()

    # fila.enfileirar(grafo.arad)
    # fila.enfileirar(grafo.bucharest)
    # fila.enfileirar(grafo.fagaras)

    # print(fila.primeiro().rotulo)
    # print(fila.desenfileirar().rotulo)
    # print(fila.primeiro().rotulo)

    # busca_largura = BuscaLargura(grafo.arad)
    # busca_largura.buscar()
    #
    # print(busca_largura.fila.numero_elementos)

    # vetor = VetorOrdenado(5)
    # vetor.insere(grafo.arad)
    # vetor.insere(grafo.craiova)
    # vetor.insere(grafo.bucharest)
    # vetor.insere(grafo.dobreta)
    # vetor.imprime()
    #
    # busca_gulosa = BuscaGulosa(grafo.bucharest)
    # busca_gulosa.buscar(grafo.arad)

    print(grafo.arad.adjacentes[0].vertice.rotulo)

    busca_aestrela = AEstrela(grafo.bucharest)
    busca_aestrela.buscar(grafo.arad)




