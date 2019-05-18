#!/usr/bin/python
import math
import numpy as np 
import scipy
from collections import deque
import sys
from tarjan import *

graph1 = [[1,2],[2],[3],[]]
graph2 = [[1,2,4],[3],[0,3,5],[],[4,5],[4]]
graph3 = [[1,3],[],[1,4],[5],[2,3],[]]
graph4 = [[1,2,3],[2,5],[4],[],[],[6],[]]



# INSERER LE GRAPHE TEST DANS CETTE VARIABLE "GRAPH"
GRAPH = graph2



print("\ntest sur graphe suivant :", GRAPH)
#----------------------------------------------------------------------------------------------
# | Construit la MATRICE D ADJACENCE
# | input : matrice étudiée
def adjacence(matr):
    adj_matrix = np.zeros((len(matr),len(matr)))  # initialise matrice vierge de même dimension
    for (i , sommet) in enumerate(matr):
        for (j , nex) in enumerate(sommet):
            adj_matrix[i][nex]=1
    return adj_matrix

#----------------------------------------------------------------------------------------------
# | Construit la matrice de FERMETURE TRANSITIVE
# | Input : matrice d'adjacence
def transitiveClosure(adj_matr):
    for (i, colonne) in enumerate(adj_matr):
        for (k, valeur) in enumerate(colonne):
            if adj_matr[i][k] == 1 :
                for (k, valeur) in enumerate(colonne):
                    if colonne[k] == 1 :                            # si transitivité, j'additionne la ligne k avec la ligne i
                        adj_matr[i] = adj_matr[i] + adj_matr[k]  # permet de ne pas toucher aux zeros
                    else:
                        continue
            else:
                continue
    # | je reattribue la valeur 1 dans les cases differentes de zero
    for (i, colonne) in enumerate(adj_matr):
        for (k, valeur) in enumerate(colonne):
            if adj_matr[i][k] >= 1:
                adj_matr[i][k] = 1
    ferm_trans = adj_matr
    return ferm_trans
#----------------------------------------------------------------------------------------------
# TEST matrice d adjacente et fermeture transitive
adj_mat = adjacence(GRAPH)
adj_mat = adj_mat.astype(int)
print("\nmatrice d'adjacence\n", adj_mat)
trans_mat = transitiveClosure(adj_mat)
print("\nfermeture transitive\n", trans_mat, "\n")
#----------------------------------------------------------------------------------------------
# DEEP FIRST SEARCH
# input : Graphe (liste de liste) | SOLUTION FONCTIONNE MAIS INEXACTE
visited = []
def dfs4(graph, sommet):
    global visited 
    if sommet not in visited:
        visited.append(sommet)
        for (i, voisins) in enumerate(graph[sommet]):
            dfs4(graph, voisins)
    return visited

print("Deep First Search | sommets parcourus :\n", dfs4(GRAPH,0))
#----------------------------------------------------------------------------------------------
# COMPOSANTE FORTEMENT CONNEXES
# Rechercher les composantes fortement connexes : algo de propagation des + et -
# On utilisera l algo DFS (Deep First Search) pour propager les +
# Ensuite on contruira la matrice d adjacence des predecesseurs et on l utilisera l algo DFS
# pour la propagation des -


