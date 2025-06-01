class Adjacente:

    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo


class AdjacenteG:

    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo
