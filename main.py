""" Arquivo main do projeto, recomendo para análise utilizar o openFile("testemenor.gr") pois o arquivo é menor e mais fácil de enxergar os resultados.
    O arquivo testemenor.gr é apenas uma cópia das primeiras 30 linhas do arquivo "USA-road-d.NY.gr", Por isso o arquivo "testemenor.gr" é um grafo desconexo,
    porém para visualizar os resultados ele serve bem.
    Se quiser trocar o arquivo, basta descomentar um e comentar o outro.
    Por padrão todos os métodos vão printar os resultados no terminal, para desativar basta comentar o print.
    Por padrão também todos os métodos vão escrever em um arquivo .txt, para desativar basta comentar o write.
"""


from Digraph import Digraph


# função que lê o arquivo .gr e retorna uma lista de arestas
def openFile(path):
    graphfile = open(path, "r")
    edges = []
    for line in graphfile.readlines():  # para cada linha do arquivo
        if line[0] == "a":
            line = line.split()  # separa a linha em uma lista
            edges.append(
                (int(line[1]), int(line[2]), int(line[3]))
            )  # adiciona a aresta na lista de arestas
    return edges


if __name__ == "__main__":
    graph = Digraph()  # cria o grafo

    # edges = openFile("USA-road-d.NY.gr") #carrega o arquivo grande
    # edges = openFile("teste.gr") #carrega um arquivo menor para teste
    edges = openFile("testemenor.gr")  # carrega um arquivo menor ainda para teste

    for edge in edges:
        graph.addAresta(edge[0], edge[1], edge[2])

    # printa as informações do grafo
    print("Vertices: ", graph.getVerticesNumber())
    print("Edges: ", graph.getEdgesNumber())
    print("Vizinhos de 1: ", graph.getVizinhanca(1))
    print("Grau Mínimo: ", graph.getGrauMinimo())
    print("Grau Máximo: ", graph.getGrauMaximo())

    # Breadth First Search
    bfsPi, bfsDistance = graph.bfs(1)
    print("BFS - pi: ", bfsPi, "\nBFS - distance: ", bfsDistance)
    bfs = open("BFSResult.txt", "w")
    bfs.write("BFS - pi: " + str(bfsPi) + "\nBFS - distance: " + str(bfsDistance))
    bfs.close()

    # Depth First Search
    visited, tInicial, tFinal = graph.dfs(1)
    print("DFS - pi: ", visited)
    print("DFS - tInicial: ", tInicial)
    print("DFS - tFinal: ", tFinal)

    dfs = open("DFSResult.txt", "w")
    dfs.write(
        "DFS - pi: "
        + str(visited)
        + "\ntInicial: "
        + str(tInicial)
        + "\ntFinal :"
        + str(tFinal)
    )
    dfs.close()

    # Bellman Ford
    bfPI, bfDistance = graph.bellmanFord(1)
    print("BF - pi: ", bfPI, "\nBF - distance: ", bfDistance)
    bf = open("BFResult.txt", "w")
    bf.write("BF - pi: " + str(bfPI) + "\nBF - distance: " + str(bfDistance))
    bf.close()

    # Dijkstra
    dijkstra, dijkstraDist = graph.dijkstra(1)
    print("Dijkstra - Pi: ", dijkstra)
    print("Dijkstra - Distance: ", dijkstraDist)
    dij = open("DijkstraResult.txt", "w")
    dij.write("Dijkstra - Pi: " + str(dijkstra))
    dij.close()

    # distancia maxima de um vértice especifico.
    distance = graph.getMaxDistance(1)
    print("Max distance vertice from 1:", distance[0], "Distance:", distance[1])
