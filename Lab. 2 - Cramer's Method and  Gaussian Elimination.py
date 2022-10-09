#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: AlessandroVavala
"""

"""
Using the Cramer's method, solve the given system of linear equations:
10x + 40x2 + 70x3 = 300
20x + 50x2 + 80x3 = 360
30x + 60x2 + 80x3 = 390
"""

import numpy as np

a = np.array([[10, 40, 70],
             [20, 50, 80],
             [30, 60, 80]])

b = np.array([300, 360, 390])

def cramer(mat, constant):
    
    D = np.linalg.det(mat) # determinant
    
    # substitution of columns with constants
    mat1 = np.array([constant, mat[:,1], mat[:,2]])
    mat2 = np.array([mat[:,0], constant, mat[:,2]])
    mat3 = np.array([mat[:,0], mat[:,1], constant])   
    
    # determinant of new matrices
    D1 = np.linalg.det(mat1)
    D2 = np.linalg.det(mat2)
    D3 = np.linalg.det(mat3)
    
    # calculus of Xs
    X1 = round(D1/D)
    X2 = round(D2/D)
    X3 = round(D3/D)
    
    print([X1, X2, X3])

cramer(a, b)

# check if the result is correct

print(np.linalg.solve(a, b))

#############################################################

"""
Solve the system of equations from ex.1 using the Gaussian elimination method.
10x + 40x2 + 70x3 = 300
20x + 50x2 + 80x3 = 360
30x + 60x2 + 80x3 = 390
"""

def gaussian_elimination(A, b):
    n = len(b)
    x = np.zeros(n) # initializing x

    # forward elimination
    # a_ij = (a_ij - a_ik/a_kk) * a_kj
    # k: diagonals (goes from 0 to n-2)
    # i: rows (goes from k+1 to n-1)
    # j: cols (k to n-1)

    for k in range (0, n-1): # loop over diagonals
        for i in range (k+1, n): # loop over the rows
            ratio = A[i, k]/A[k, k] # does not dipends from j
            for j in range (k, n): # loop over the elements (cols) of the rows
                A[i, j] -= ratio*A[k, j] # update the elements using the ratio multiplied the diagonal.
                                            
            b[i] -= ratio*b[k] # updating b-vector        

    # back substitution
    # x_n-1 = b_n-1/A_n-1, n-1
    # x_i = (b_i - sum_j (a_ij * x_j))/a_ii
    # i = n-2 to 0
    # j = i+1 to n-1

    x[n-1] = b[n-1]/A[n-1, n-1]
    for i in range (n-2,-1, -1): # loop over the rows from bottom to top
        sum_j = 0
        for j in range (i+1, n):
            sum_j += A[i,j]*x[j]
        x[i] = (b[i]- sum_j)/A[i,i]
    
    print(A)
    print("")
    print(b)
    print("")
    print(x)
    
gaussian_elimination(a, b)

"""
A system of linear equations is given:
x + 2x2 + 2x3 = 1
3x + 3x2 = 3
x + x3 = 2
Check if the matrix A of the given system is singular, if not then solve the system by Gaussian elimination.
"""

a = np.array([[1, 2 , 2],
             [3, 3, 0],
             [1, 0, 1]])

b = np.array([1, 3, 2])

def check(A, b):
    if np.linalg.det(A) == 0:
        print("Singular Matrix")
    else:
        gaussian_elimination(A, b)

check(a, b)


