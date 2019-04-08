#!/usr/bin/python

import mpmath
import numpy as np 
import scipy

graph = [[1,2],[2],[3],[]]

test = [[1,2,4],[3],[0,3,5],[],[4,5],[4]]

exo = [[1,3],[],[1,4],[5],[2,3],[]]

# Initialise une matrice vierge de même taille que la matrice étudiée
def new_matrix(matr):
    virgin_matrix = np.zeros((len(matr),len(matr)))
    return virgin_matrix

# Construit la matrice d'adjacence
# input : matrice étudiée, matrice vierge de même dimension
def adjacence(matr,virgin_matr):
    adj_matrix = virgin_matr
    for (i , sommet) in enumerate(matr):
        for (j , nex) in enumerate(sommet):
            adj_matrix[i][nex]=1
    return adj_matrix

# adj_matrix_sauvegarde = adjacence(test,new_matrix(test))

# Construit la matrice de fermeture transitive
# Input : matrice d'adjacence
def transitiveClosure(ferm_trans):
    for (i, colonne) in enumerate(ferm_trans):
        for (k, valeur) in enumerate(colonne):
            if ferm_trans[i][k] == 1 :
                for (k, valeur) in enumerate(colonne):
                    if colonne[k] == 1 :
                        ferm_trans[i] = ferm_trans[i] + ferm_trans[k]
                    else:
                        continue
            else:
                continue

    for (i, colonne) in enumerate(ferm_trans):
        for (k, valeur) in enumerate(colonne):
            if ferm_trans[i][k] >= 1:
                ferm_trans[i][k] = 1
    return ferm_trans

# print("matrice d'adjacence\n", adj_matrix_sauvegarde)
# res = transitiveClosure(adj_matrix_sauvegarde)
# print("matrice de fermeture transitive", res)

sauve_exo = adjacence(exo, new_matrix(exo))
print(sauve_exo)
res_exo = transitiveClosure(sauve_exo)
print(res_exo)
