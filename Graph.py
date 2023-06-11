class Graph:
    def __init__(self):
        self.adjacencyList = {}
        self.arestas = []

    def addVertice(self, vertice):
        if vertice not in self.adjacencyList:
            self.adjacencyList[vertice] = []

    def addAresta(self, origem, destino, peso):
        self.addVertice(origem)
        self.addVertice(destino)
        self.arestas.append((origem, destino, peso))
        self.adjacencyList[origem].append((destino, peso))
        self.adjacencyList[destino].append((origem, peso))
        

    def getVerticesNumber(self):
        return len(self.adjacencyList)

    def getEdgesNumber(self):
        return len(self.arestas)

    def getVizinhanca(self, vertice):
        if vertice in self.adjacencyList:
            return [vizinho for vizinho, _ in self.adjacencyList[vertice]]
        return []

    def getGrau(self, vertice):
        if vertice in self.adjacencyList:
            return len(self.adjacencyList[vertice])
        return 0

    def getGrauMaximo(self):
        grauMaximo = 0
        for vertice in self.adjacencyList:
            grau = len(self.adjacencyList[vertice])
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
        for vertice in self.adjacencyList:
            grau = len(self.adjacencyList[vertice])
            if grau < grauMinimo:
                grauMinimo = grau
        return grauMinimo
    
    