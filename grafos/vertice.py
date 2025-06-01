class Vertice:

    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []

    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostrar_adjacentes(self):
        for item in range(len(self.adjacentes)):
            print(self.adjacentes[item].vertice.rotulo, self.adjacentes[item].custo)


class VerticeG:

    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostrar_adjacentes(self):
        for item in range(len(self.adjacentes)):
            print(self.adjacentes[item].vertice.rotulo, self.adjacentes[item].custo)
