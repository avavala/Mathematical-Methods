#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:02:12 2022

@author: AlessandroVavala
"""
import copy
def get_matrix_minor(a,i):#FUNCTION TO FIND THE NEW MATRIX
    matrix = copy.deepcopy(a) #to make a perfect copy of the matrix
    order = len(matrix)
    if order == 2:
        
        return matrix
    else:
        matrix.pop(0)
        for j in matrix: 
            j.pop(i) #remove the ith element
            
        return matrix
    
def get_determinant(a):#FUNCTION TO FIND THE DETERMINANT OF A MATRIX
    order = len(a)
    if order == 2: #check if the matrix is order of 2
        det = a[0][0]*a[1][1] - a[1][0]*a[0][1]
        return det
        
    else: 
        det = 0
        for i in range(len(a[0])):
            det += ((-1)**i)*a[0][i]*get_determinant(get_matrix_minor(a,i)) #recursive function
            return det        

A = [[1,2],[3,4]]
B = [[1,2,3],[4,5,6],[7,8,9]]
print("Determinant of A --> ",get_determinant(A))
print("Determinant of B --> ",get_determinant(B))