from graphLib import Grafo

def openFile(path):
    graphfile = open(path, 'r')
    edges = []
    for line in graphfile.readlines():
        if line[0] == 'a':
            line = line.split()
            edges.append((int(line[1]), int(line[2]), int(line[3])))
    return edges
    

if __name__ == '__main__':
    graph = Grafo()
    
    edges = openFile('USA-road-d.NY.gr')
        
    for edge in edges:
        graph.addAresta(edge[0], edge[1], edge[2])
    
    print(graph.getGrauMinimo())