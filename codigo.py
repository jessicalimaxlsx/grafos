# Abre o arquivo <arquivo.g> no modo leitura
arquivo = open("C:/Users/Jessica/Documents/Código Nécio/arquivo.txt", "r")

'''
# Legenda dos vértices
1- Viçosa do Ceará
2- Tianguá
3- Ubajara
4- Ibiapina
5- São Benedito
6- Carnaubal
7- Guaraciaba
8- Croatá
9- Ipú
'''

# Le a primeira linha do arquivo, que contém o número de vértices que vem depois
n = int(arquivo.readline())

# Cria uma matriz de adjacência vazia
matriz = [[0 for i in range(n)] for j in range(n)]

# Le as demais linhas do arquivo, que contêm os vertices e os pesos das arestas
for linha in arquivo:
  # Separa os valores da linha por espaços em branco
  valores = linha.split()
  # Converte os valores para inteiros (arredondamos os valores que coletamos)
  x = int(valores[0]) # Primeira cidade
  y = int(valores[1]) # Segunda cidade
  z = int(valores[2]) # Distancia entre as cidaddes
  # Preenche a matriz de adjacência com os valores
  matriz[x-1][y-1] = z # Aresta de x para y
  matriz[y-1][x-1] = z # Aresta de y para x (eh pra ser um grafo não direcionado pq é pra qualquer direção)

# Fecha o arquivo que a gente leu
arquivo.close()

# Exibe a matriz de adjacência na tela
print("Matriz de adjacência do grafo:")
for i in range(n):
  for j in range(n):
    print(matriz[i][j], end=" ") # Exibe a matriz (ATENÇÃO: ver de deixar ela formatada no futuro)
  print() # Quebra a linha pois vai ter mais uma pergunta pro user

############# TENTATIVA DE GRAFICO VISUAL SEJA OQ DEUS QUISER ############

import networkx as nx
import matplotlib.pyplot as plt

# Ativar o modo interativo pra poder digitar no terminal enquanto o grafico ta rodando, se nao o usuario n consegue
plt.ion()

# Criar um gráfico vazio
G = nx.Graph()

# Adicionar as cidade
cidades = ['Viçosa do Ceará', 'Tianguá', 'Ubajara', 'Ibiapina', 'São Benedito', 'Carnaubal', 'Guaraciaba', 'Croatá', 'Ipú']
G.add_nodes_from(cidades)

# Adicionar as conexoes entre as cidade
arestas = [('Viçosa do Ceará', 'Tianguá', 31), ('Tianguá', 'Ubajara', 17), ('Ubajara', 'Ibiapina', 9), ('Ibiapina', 'São Benedito', 14), ('São Benedito', 'Carnaubal', 19), ('São Benedito', 'Guaraciaba', 23), ('Carnaubal', 'Guaraciaba', 25), ('Carnaubal', 'Croatá', 41), ('Guaraciaba', 'Croatá', 37), ('Guaraciaba', 'Ipú', 27), ('Croatá', 'Ipú', 46)]
G.add_weighted_edges_from(arestas)

# Definir posições
pos = {'Viçosa do Ceará': (0,5),
       'Tianguá': (0,4),
       'Ubajara': (0,3),
       'Ibiapina': (0,2),
       'São Benedito': (0,1),
       'Carnaubal': (-1,0),
       'Guaraciaba': (1,0),
       'Croatá': (-1,-1),
       'Ipú': (1,-1)}

# Desenhar o graf
nx.draw(G,pos, with_labels=False, node_color=['red','green','blue','cyan','magenta','yellow','pink','purple','orange'], node_size=1000)


# Tentar eixar os rótulos bonitos
labels = nx.get_edge_attributes(G,'weight')
label_pos = 0.3 # da pra mudar se vcs nao gostar 
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,label_pos=label_pos)

# mudar as posiçao dos rotulos das cidades para evitar ficar em cima da distancia
city_labels_pos = {city:(x,y+0.1) for city,(x,y) in pos.items()} # Ajuste o valor 0.1 conforme necessário
nx.draw_networkx_labels(G,city_labels_pos)

plt.axis('off')
plt.show()

#######################