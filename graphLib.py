class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []

    def addVertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def addAresta(self, origem, destino, peso):
        self.addVertice(origem)
        self.addVertice(destino)
        self.arestas.append((origem, destino, peso))
        self.vertices[origem].append((destino, peso))
        # self.vertices[destino].append((origem, peso))

    def getVerticesNumber(self):
        return len(self.vertices)

    def getEdgesNumber(self):
        return len(self.arestas)

    def getVizinhanca(self, vertice):
        if vertice in self.vertices:
            return [vizinho for vizinho, _ in self.vertices[vertice]]
        return []

    def getGrau(self, vertice):
        if vertice in self.vertices:
            return len(self.vertices[vertice])
        return 0

    def getGrauMaximo(self):
        grauMaximo = 0
        for vertice in self.vertices:
            grau = len(self.vertices[vertice])
            if grau > grauMaximo:
                grauMaximo = grau
        return grauMaximo

    def getPeso(self, origem, destino):
        for aresta in self.arestas:
            if (aresta[0] == origem and aresta[1] == destino) or (aresta[0] == destino and aresta[1] == origem):
                return aresta[2]
        return None

    def getGrauMinimo(self):
        grauMinimo = float('inf')
        for vertice in self.vertices:
            grau = len(self.vertices[vertice])
            if grau < grauMinimo:
                grauMinimo = grau
        return grauMinimo
    
    