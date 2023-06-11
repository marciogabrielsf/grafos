from Digraph import Digraph

def openFile(path):
    graphfile = open(path, 'r')
    edges = []
    for line in graphfile.readlines():
        if line[0] == 'a':
            line = line.split()
            edges.append((int(line[1]), int(line[2]), int(line[3])))
    return edges
    

if __name__ == '__main__':
    graph = Digraph()
    
    edges = openFile('USA-road-d.NY.gr')
    # edges = openFile('teste.gr')
        
    for edge in edges:
        graph.addAresta(edge[0], edge[1], edge[2])
    


    
    # graph.addAresta(1, 2, 1)
    # graph.addAresta(2, 3, 10)
    
    
    
    print("Vertices: " , graph.getVerticesNumber())
    print('Edges: ', graph.getEdgesNumber())
    print('Grau Mínimo: ', graph.getGrauMinimo())
    print('Grau Máximo: ', graph.getGrauMaximo())
    print('Grau do vértice 1: ', graph.getGrau(1))