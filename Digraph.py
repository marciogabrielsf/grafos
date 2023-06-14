class Digraph:
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
            if (aresta[0] == origem and aresta[1] == destino) or (
                aresta[0] == destino and aresta[1] == origem
            ):
                return aresta[2]
        return None

    def getGrauMinimo(self):
        grauMinimo = float("inf")
        for vertice in self.adjacencyList:
            grau = len(self.adjacencyList[vertice])
            if grau < grauMinimo:
                grauMinimo = grau
        return grauMinimo

    def bfs(self, origem, destino):
        visited = [origem]
        queue = [origem]

        while queue:
            vertice = queue.pop(0)
            if vertice == destino:
                return visited, len(visited) - 1
            for vizinho, _ in self.adjacencyList[vertice]:
                if vizinho not in visited:
                    visited.append(vizinho)
                    queue.append(vizinho)
        return [], 0

    def dfs(self, visited, node, timeInicio, timeFim, tempo):
        if tempo is None:
            tempo = 0
        if timeInicio is None:
            timeInicio = {}
        if timeFim is None:
            timeFim = {}
        if visited is None:
            visited = set()

        if node not in visited:
            visited.add(node)
            timeInicio[node] = [tempo]
            timeFim[node] = []
            tempo += 1

            for vizinho, _ in self.adjacencyList[node]:
                self.dfs(visited, vizinho, timeInicio, timeFim, tempo)
                tempo += 1
            timeFim[node].append(tempo)

        return visited, timeInicio, timeFim, tempo

    def bellmanFord(self, origem):
        dist = {}
        for vertice in self.adjacencyList:
            dist[vertice] = float("inf")
        dist[origem] = 0

        for _ in range(self.getVerticesNumber() - 1):
            for origem, destino, peso in self.arestas:
                if dist[origem] != float("inf") and dist[origem] + peso < dist[destino]:
                    dist[destino] = dist[origem] + peso

        for origem, destino, peso in self.arestas:
            if dist[origem] != float("inf") and dist[origem] + peso < dist[destino]:
                return False

        return dist
