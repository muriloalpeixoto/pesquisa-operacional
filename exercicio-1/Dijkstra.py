from Grafo import Grafo
import sys

def algoritmo_dijkstra(grafo, vertice_inicial):
    vertices_nao_visitados = list(grafo.get_vertices())
 
    # Aqui usaremos um dicionário do python para armazenar o custo de visitar cada nó e atualiza-lo confome vamos nos movimentando ao longo do grafo.
    caminho_mais_curto = {}
 
    # Usaremos este dicionário para salvar o caminho mais curto conhecido para um nó encontrado até agora
    vertices_previos = {}
 
    # Usaremos valor_maximo para inicializar o valor "infinito" dos nós não visitados  
    valor_maximo = sys.maxsize
    for vertice in vertices_nao_visitados:
        caminho_mais_curto[vertice] = valor_maximo
    # No entanto, inicializamos o valor do vértice inicial com 0  
    caminho_mais_curto[vertice_inicial] = 0
    
    # O algoritmo é executado até que visitemos todos os nós
    while vertices_nao_visitados:
        # O bloco de código abaixo encontra o vértice com a pontuação mais baixa
        vertice_minimo_atual = None
        for vertice in vertices_nao_visitados: # Iterar sobre os vértices
            if vertice_minimo_atual == None:
                vertice_minimo_atual = vertice
            elif caminho_mais_curto[vertice] < caminho_mais_curto[vertice_minimo_atual]:
                vertice_minimo_atual = vertice
                
        # O bloco de código abaixo recupera os vizinhos do vértice atual e atualiza suas distâncias
        vizinhos = grafo.get_arestas_saida(vertice_minimo_atual)
        for vizinho in vizinhos:
            valor_tentativa = caminho_mais_curto[vertice_minimo_atual] + grafo.valor_aresta(vertice_minimo_atual, vizinho)
            if valor_tentativa < caminho_mais_curto[vizinho]:
                caminho_mais_curto[vizinho] = valor_tentativa
                # Também atualizamos o melhor caminho para o vértice atual
                vertices_previos[vizinho] = vertice_minimo_atual
 
        # Depois de visitar seus vizinhos, marcamos o vértice como "visitado"
        vertices_nao_visitados.remove(vertice_minimo_atual)
    
    return vertices_previos, caminho_mais_curto

def resultado(vertices_previos, caminho_mais_curto, vertice_inicial, vertice_destino):
    caminho = []
    vertice = vertice_destino
    
    while vertice != vertice_inicial:
        caminho.append(vertice)
        vertice = vertices_previos[vertice]
 
    # Adicione o vértice inicial manualmente
    caminho.append(vertice_inicial)
    
    print("Encontramos o melhor caminho com o peso total de We found the following best caminho with a value of {}.".format(caminho_mais_curto[vertice_destino]))
    print(" -> ".join(reversed(caminho)))


vertices = ["1", "2", "3", "4", "5", "6", "7"]
grafos_init = {}
for vertice in vertices:
    grafos_init[vertice] = {}

grafos_init["1"]["2"] = 2
grafos_init["1"]["3"] = 5
grafos_init["1"]["4"] = 4
grafos_init["2"]["5"] = 7
grafos_init["2"]["3"] = 3
grafos_init["3"]["5"] = 4
grafos_init["3"]["6"] = 3
grafos_init["3"]["4"] = 1
grafos_init["4"]["6"] = 4
grafos_init["5"]["7"] = 1
grafos_init["5"]["6"] = 5
grafos_init["6"]["7"] = 7

grafo = Grafo(vertices, grafos_init)
vertices_previos, caminho_mais_curto = algoritmo_dijkstra(grafo=grafo, vertice_inicial="1")
resultado(vertices_previos, caminho_mais_curto, vertice_inicial="1", vertice_destino="7")
