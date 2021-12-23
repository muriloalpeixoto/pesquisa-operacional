import sys
 
class Grafo(object):
    def __init__(self, vertices, init_grafo):
        self.vertices = vertices
        self.grafo = self.construct_grafo(vertices, init_grafo)
        
    def construct_grafo(self, vertices, init_grafo):
        '''
        Este método assegura que o grafo é simétrico. Em outras palavras, se existe um caminho partido do vértice A chegando ao vértice B 
        com um valor V, é seguro que existe um caminho partindo do vértice B chegando ao vértice A com um valor também igual a V.
        '''
        grafo = {}
        for vertice in vertices:
            grafo[vertice] = {}
        
        grafo.update(init_grafo)
        
        for vertice, arestas in grafo.items():
            for vertice_adjacente, value in arestas.items():
                if grafo[vertice_adjacente].get(vertice, False) == False:
                    grafo[vertice_adjacente][vertice] = value
                    
        return grafo
    
    def get_vertices(self):
        "Retorna os vértices do grafo."
        return self.vertices
    
    def get_arestas_saida(self, vertice):
        "Retorna os vizinhos de um vertice."
        conexoes = []
        for out_vertice in self.vertices:
            if self.grafo[vertice].get(out_vertice, False) != False:
                conexoes.append(out_vertice)
        return conexoes
    
    def valor_aresta(self, vertice1, vertice2):
        "Retorna o valor de uma aresta entre dois vertices."
        return self.grafo[vertice1][vertice2]