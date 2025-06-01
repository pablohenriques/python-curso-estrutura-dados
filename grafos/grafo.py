from grafos.adjacente import Adjacente, AdjacenteG
from grafos.vertice import Vertice, VerticeG


class Grafo:

    arad = Vertice('Arad')
    zerind = Vertice('Zerind')
    oradea = Vertice('Oradea')
    sibiu = Vertice('Sibiu')
    timisoara = Vertice('Timisoara')
    lugoj = Vertice('Lugoj')
    mehadia = Vertice('Mehadia')
    dobreta = Vertice('Dobreta')
    craiova = Vertice('Craiova')
    rimnicu = Vertice('Rimnicu')
    fagaras = Vertice('Fagaras')
    pitesti = Vertice('Pitesti')
    bucharest = Vertice('Bucharest')
    giurgiu = Vertice('Giurgiu')

    arad.adicionar_adjacente(Adjacente(zerind, 75))
    arad.adicionar_adjacente(Adjacente(sibiu, 140))
    arad.adicionar_adjacente(Adjacente(timisoara, 118))

    zerind.adicionar_adjacente(Adjacente(arad, 75))
    zerind.adicionar_adjacente(Adjacente(oradea, 71))

    oradea.adicionar_adjacente(Adjacente(zerind, 71))
    oradea.adicionar_adjacente(Adjacente(sibiu, 151))

    sibiu.adicionar_adjacente(Adjacente(oradea, 151))
    sibiu.adicionar_adjacente(Adjacente(arad, 140))
    sibiu.adicionar_adjacente(Adjacente(fagaras, 99))
    sibiu.adicionar_adjacente(Adjacente(rimnicu, 80))

    timisoara.adicionar_adjacente(Adjacente(arad, 118))
    timisoara.adicionar_adjacente(Adjacente(lugoj, 111))

    lugoj.adicionar_adjacente(Adjacente(timisoara, 111))
    lugoj.adicionar_adjacente(Adjacente(mehadia, 70))

    mehadia.adicionar_adjacente(Adjacente(lugoj, 70))
    mehadia.adicionar_adjacente(Adjacente(dobreta, 75))

    dobreta.adicionar_adjacente(Adjacente(mehadia, 75))
    dobreta.adicionar_adjacente(Adjacente(craiova, 120))

    craiova.adicionar_adjacente(Adjacente(dobreta, 120))
    craiova.adicionar_adjacente(Adjacente(pitesti, 138))
    craiova.adicionar_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adicionar_adjacente(Adjacente(craiova, 146))
    rimnicu.adicionar_adjacente(Adjacente(sibiu, 80))
    rimnicu.adicionar_adjacente(Adjacente(pitesti, 97))

    fagaras.adicionar_adjacente(Adjacente(sibiu, 99))
    fagaras.adicionar_adjacente(Adjacente(bucharest, 211))

    pitesti.adicionar_adjacente(Adjacente(rimnicu, 97))
    pitesti.adicionar_adjacente(Adjacente(craiova, 138))
    pitesti.adicionar_adjacente(Adjacente(bucharest, 101))

    bucharest.adicionar_adjacente(Adjacente(fagaras, 211))
    bucharest.adicionar_adjacente(Adjacente(pitesti, 101))
    bucharest.adicionar_adjacente(Adjacente(giurgiu, 90))


class GrafoG:
  arad = VerticeG('Arad', 366)
  zerind = VerticeG('Zerind', 374)
  oradea = VerticeG('Oradea', 380)
  sibiu = VerticeG('Sibiu', 253)
  timisoara = VerticeG('Timisoara', 329)
  lugoj = VerticeG('Lugoj', 244)
  mehadia = VerticeG('Mehadia', 241)
  dobreta = VerticeG('Dobreta', 242)
  craiova = VerticeG('Craiova', 160)
  rimnicu = VerticeG('Rimnicu', 193)
  fagaras = VerticeG('Fagaras', 178)
  pitesti = VerticeG('Pitesti', 98)
  bucharest = VerticeG('Bucharest', 0)
  giurgiu = VerticeG('Giurgiu', 77)

  arad.adicionar_adjacente(Adjacente(zerind, 75))
  arad.adicionar_adjacente(Adjacente(sibiu, 140))
  arad.adicionar_adjacente(Adjacente(timisoara, 118))

  zerind.adicionar_adjacente(Adjacente(arad, 75))
  zerind.adicionar_adjacente(Adjacente(oradea, 71))

  oradea.adicionar_adjacente(Adjacente(zerind, 71))
  oradea.adicionar_adjacente(Adjacente(sibiu, 151))

  sibiu.adicionar_adjacente(Adjacente(oradea, 151))
  sibiu.adicionar_adjacente(Adjacente(arad, 140))
  sibiu.adicionar_adjacente(Adjacente(fagaras, 99))
  sibiu.adicionar_adjacente(Adjacente(rimnicu, 80))

  timisoara.adicionar_adjacente(Adjacente(arad, 118))
  timisoara.adicionar_adjacente(Adjacente(lugoj, 111))

  lugoj.adicionar_adjacente(Adjacente(timisoara, 111))
  lugoj.adicionar_adjacente(Adjacente(mehadia, 70))

  mehadia.adicionar_adjacente(Adjacente(lugoj, 70))
  mehadia.adicionar_adjacente(Adjacente(dobreta, 75))

  dobreta.adicionar_adjacente(Adjacente(mehadia, 75))
  dobreta.adicionar_adjacente(Adjacente(craiova, 120))

  craiova.adicionar_adjacente(Adjacente(dobreta, 120))
  craiova.adicionar_adjacente(Adjacente(pitesti, 138))
  craiova.adicionar_adjacente(Adjacente(rimnicu, 146))

  rimnicu.adicionar_adjacente(Adjacente(craiova, 146))
  rimnicu.adicionar_adjacente(Adjacente(sibiu, 80))
  rimnicu.adicionar_adjacente(Adjacente(pitesti, 97))

  fagaras.adicionar_adjacente(Adjacente(sibiu, 99))
  fagaras.adicionar_adjacente(Adjacente(bucharest, 211))

  pitesti.adicionar_adjacente(Adjacente(rimnicu, 97))
  pitesti.adicionar_adjacente(Adjacente(craiova, 138))
  pitesti.adicionar_adjacente(Adjacente(bucharest, 101))

  bucharest.adicionar_adjacente(Adjacente(fagaras, 211))
  bucharest.adicionar_adjacente(Adjacente(pitesti, 101))
  bucharest.adicionar_adjacente(Adjacente(giurgiu, 90))

class GrafoA:
  arad = VerticeG('Arad', 366)
  zerind = VerticeG('Zerind', 374)
  oradea = VerticeG('Oradea', 380)
  sibiu = VerticeG('Sibiu', 253)
  timisoara = VerticeG('Timisoara', 329)
  lugoj = VerticeG('Lugoj', 244)
  mehadia = VerticeG('Mehadia', 241)
  dobreta = VerticeG('Dobreta', 242)
  craiova = VerticeG('Craiova', 160)
  rimnicu = VerticeG('Rimnicu', 193)
  fagaras = VerticeG('Fagaras', 178)
  pitesti = VerticeG('Pitesti', 98)
  bucharest = VerticeG('Bucharest', 0)
  giurgiu = VerticeG('Giurgiu', 77)

  arad.adicionar_adjacente(AdjacenteG(zerind, 75))
  arad.adicionar_adjacente(AdjacenteG(sibiu, 140))
  arad.adicionar_adjacente(AdjacenteG(timisoara, 118))

  zerind.adicionar_adjacente(AdjacenteG(arad, 75))
  zerind.adicionar_adjacente(AdjacenteG(oradea, 71))

  oradea.adicionar_adjacente(AdjacenteG(zerind, 71))
  oradea.adicionar_adjacente(AdjacenteG(sibiu, 151))

  sibiu.adicionar_adjacente(AdjacenteG(oradea, 151))
  sibiu.adicionar_adjacente(AdjacenteG(arad, 140))
  sibiu.adicionar_adjacente(AdjacenteG(fagaras, 99))
  sibiu.adicionar_adjacente(AdjacenteG(rimnicu, 80))

  timisoara.adicionar_adjacente(AdjacenteG(arad, 118))
  timisoara.adicionar_adjacente(AdjacenteG(lugoj, 111))

  lugoj.adicionar_adjacente(AdjacenteG(timisoara, 111))
  lugoj.adicionar_adjacente(AdjacenteG(mehadia, 70))

  mehadia.adicionar_adjacente(AdjacenteG(lugoj, 70))
  mehadia.adicionar_adjacente(AdjacenteG(dobreta, 75))

  dobreta.adicionar_adjacente(AdjacenteG(mehadia, 75))
  dobreta.adicionar_adjacente(AdjacenteG(craiova, 120))

  craiova.adicionar_adjacente(AdjacenteG(dobreta, 120))
  craiova.adicionar_adjacente(AdjacenteG(pitesti, 138))
  craiova.adicionar_adjacente(AdjacenteG(rimnicu, 146))

  rimnicu.adicionar_adjacente(AdjacenteG(craiova, 146))
  rimnicu.adicionar_adjacente(AdjacenteG(sibiu, 80))
  rimnicu.adicionar_adjacente(AdjacenteG(pitesti, 97))

  fagaras.adicionar_adjacente(AdjacenteG(sibiu, 99))
  fagaras.adicionar_adjacente(AdjacenteG(bucharest, 211))

  pitesti.adicionar_adjacente(AdjacenteG(rimnicu, 97))
  pitesti.adicionar_adjacente(AdjacenteG(craiova, 138))
  pitesti.adicionar_adjacente(AdjacenteG(bucharest, 101))

  bucharest.adicionar_adjacente(AdjacenteG(fagaras, 211))
  bucharest.adicionar_adjacente(AdjacenteG(pitesti, 101))
  bucharest.adicionar_adjacente(AdjacenteG(giurgiu, 90))