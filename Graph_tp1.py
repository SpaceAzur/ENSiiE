#!/usr/bin/python

import mpmath
import numpy as np 
import scipy

graph1 = [[1,2],[2],[3],[]]

graph2 = [[1,2,4],[3],[0,3,5],[],[4,5],[4]]

graph3 = [[1,3],[],[1,4],[5],[2,3],[]]

# | Construit la matrice d'adjacence
# | input : matrice étudiée
def adjacence(matr):
    adj_matrix = np.zeros((len(matr),len(matr)))  # initialise matrice vierge de même dimension
    for (i , sommet) in enumerate(matr):
        for (j , nex) in enumerate(sommet):
            adj_matrix[i][nex]=1
    return adj_matrix

# | Construit la matrice de fermeture transitive
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

adj_mat = adjacence(graph3)
print("\nmatrice d'adjacence\n", adj_mat)
trans_mat = transitiveClosure(adj_mat)
print("\nfermeture transitive\n", trans_mat)

with open("test_graph", encoding='utf-8') as file:
    test = file.read()


