import heapq
import operator


class Digraph:
    def __init__(self):
        # inicia o dicionário de adjacencia e lista de arestas
        self.adjacencyList = {}
        self.arestas = []

    # adiciona um vértice ao grafo
    def addVertice(self, vertice):
        if (
            vertice not in self.adjacencyList
        ):  # se o vertice não está no dicionário de adjacência:
            self.adjacencyList[
                vertice
            ] = []  # adiciona o vertice ao dicionário de adjacência

    # adiciona uma aresta ao grafo
    def addAresta(self, origem, destino, peso):
        # adiciona os vértices caso não existam
        self.addVertice(origem)
        self.addVertice(destino)

        # adiciona a aresta a lista de arestas
        self.arestas.append((origem, destino, peso))

        # adiciona a aresta a lista de adjacência, adicionando o destino na origem.
        self.adjacencyList[origem].append((destino, peso))

    # retorna o número de vértices do grafo
    def getVerticesNumber(self):
        # retorna o tamanho da lista de adjacência
        return len(self.adjacencyList)

    # retorna o número de arestas do grafo
    def getEdgesNumber(self):
        # retorna o tamanho da lista de arestas
        return len(self.arestas)

    # retorna a vizinhança de um vértice
    def getVizinhanca(self, vertice):
        # se o vértice está na lista de adjacência, retorna a lista de vizinhos do vértice.
        if vertice in self.adjacencyList:
            return [vizinho for vizinho, _ in self.adjacencyList[vertice]]
        return []

    # retorna o grau de um vértice
    def getGrau(self, vertice):
        # se o vértice está na lista de adjacência, retorna o tamanho da lista de adjacência do vértice.
        if vertice in self.adjacencyList:
            return len(self.adjacencyList[vertice])
        return 0

    # retorna o grau máximo do grafo
    def getGrauMaximo(self):
        # para cada vértice na lista de adjacência, calcula o grau e retorna o maior grau encontrado.
        grauMaximo = 0
        for vertice in self.adjacencyList:
            grau = len(self.adjacencyList[vertice])
            if grau > grauMaximo:
                grauMaximo = grau
        return grauMaximo

    # retorna o peso de uma aresta
    def getPeso(self, origem, destino):
        # para cada aresta na lista de arestas do grafo, busca se a origem e o destino são iguais e printa o peso da aresta que encontrar.
        for aresta in self.arestas:
            if (aresta[0] == origem and aresta[1] == destino) or (
                aresta[0] == destino and aresta[1] == origem
            ):
                return aresta[2]
        return None

    # retorna o grau mínimo do grafo
    def getGrauMinimo(self):
        grauMinimo = float("inf")
        for vertice in self.adjacencyList:
            grau = len(self.adjacencyList[vertice])
            if grau < grauMinimo:
                grauMinimo = grau
        return grauMinimo

    # retorna o método Breadth-First Search, com uma lista pi e uma lista d
    def bfs(self, origem):
        # cria uma lista de visitados e uma fila
        visited = [origem]
        queue = [origem]

        # cria um dicionário de distâncias
        distancia = 0
        distanceList = {origem: distancia}

        # enquanto a fila não estiver vazia
        while queue:
            # remove o primeiro elemento da fila
            vertice = queue.pop(0)
            distancia += 1

            # para cada vizinho do vértice
            for vizinho, peso in self.adjacencyList[vertice]:
                if (
                    vizinho not in visited
                ):  # se o vizinho não estiver na lista de visitados
                    distanceList[vizinho] = distancia  # adiciona a distância do vizinho
                    visited.append(vizinho)  # adiciona o vizinho na lista de visitados
                    queue.append(vizinho)  # adiciona o vizinho na fila

        return visited, distanceList  # retorna a lista pi e d

    # retorna o método Depth-First Search com uma lista pi, uma lista de tempo inicial e uma lista de tempo final.
    def dfs(self, origem):
        # cria uma lista de visitados e uma pilha
        visitados, stack = [], [origem]

        # cria uma variável de tempo
        tempo = 0

        # cria um dicionário de tempo inicial e final
        tInicial = {}
        tFinal = {}

        # enquanto a pilha não estiver vazia
        while stack:
            # remove o último elemento da pilha
            vertice = stack.pop()
            visitados.append(vertice)  # adiciona o vértice na lista de visitados
            tInicial[vertice] = [tempo]  # adiciona o tempo inicial do vértice

            # para cada vizinho do vértice
            for vizinho, peso in reversed(self.adjacencyList[vertice]):
                if (
                    vizinho not in visitados
                ):  # se o vizinho não estiver na lista de visitados
                    stack.append(vizinho)  # adiciona o vizinho na pilha
                    tempo += 1
            tFinal[vertice] = [tempo]

        return visitados, tInicial, tFinal

    # retorna o método BellmanFord com uma lista pi e uma lista d
    def bellmanFord(self, origem):
        dist = {}  # cria um dicionário de distâncias
        pi = [origem]  # cria uma lista pi
        for vertice in self.adjacencyList:  # para cada vértice do grafo
            dist[vertice] = float("inf")  # adiciona a distância como infinito
        dist[origem] = 0  # adiciona a distância da origem como 0

        for _ in range(self.getVerticesNumber() - 1):  # para cada vértice do grafo
            for origem, destino, peso in self.arestas:  # para cada aresta do grafo
                if (
                    dist[origem] != float("inf") and dist[origem] + peso < dist[destino]
                ):  # se a distância da origem não for infinito e a distância da origem + o peso for menor que a distância do destino
                    dist[destino] = (
                        dist[origem] + peso
                    )  # torna a distância do destino a distância da origem + o peso
                    pi.append(destino)  # adiciona o destino na lista pi

        # para cada aresta do grafo
        for origem, destino, peso in self.arestas:
            # se a distância da origem não for infinito e a distância da origem + o peso for menor que a distância do destino
            if dist[origem] != float("inf") and dist[origem] + peso < dist[destino]:
                return False  # retorna falso

        return pi, dist  # retorna a lista pi e d

    # retorna o método Dijkstra com uma lista pi e uma lista d
    def dijkstra(self, origem):
        # cria um dicionário de distâncias e uma lista pi
        dist = {}
        pi = [origem]

        # para cada vértice do grafo
        for vertice in self.adjacencyList:
            dist[vertice] = float("inf")  # adiciona a distância como infinito
        dist[origem] = 0  # adiciona a distância da origem como 0

        # cria uma fila de prioridade
        queue = []
        # adiciona a distância da origem e a origem na fila de prioridade
        heapq.heappush(queue, (dist[origem], origem))

        # enquanto a fila de prioridade não estiver vazia
        while queue:
            # remove o primeiro elemento da fila de prioridade
            _, vertice = heapq.heappop(queue)

            # para cada vizinho do vértice
            for vizinho, peso in self.adjacencyList[vertice]:
                # se a distância do vizinho for maior que a distância do vértice + o peso
                if dist[vizinho] > dist[vertice] + peso:
                    # torna a distância do vizinho a distância do vértice + o peso
                    dist[vizinho] = (
                        dist[vertice] + peso
                    )  # atualiza a distância do vizinho
                    pi.append(vizinho)  # adiciona o vizinho na lista pi
                    heapq.heappush(
                        queue, (dist[vizinho], vizinho)
                    )  # adiciona a distância do vizinho e o vizinho na fila de prioridade
        return pi, dist

    # retorna a maior distância de um vértice para os demais utilizando o método de Dijkstra
    def getMaxDistance(self, origem):
        list = {}
        _, dijkstra = self.dijkstra(
            origem
        )  # capta todas as distancias que o algoritmo de dijkstra calculou

        # para cada vertice que o algoritmo captou, remover os infinitos e adicionar no dicionario (para evitar que retorne "inf" em grafos desconexos.)
        for vertice in dijkstra:
            if dijkstra[vertice] != float("inf"):
                list[vertice] = dijkstra[vertice]

        # retorna o maior valor da lista filtrada.
        return max(list.items(), key=operator.itemgetter(1))
