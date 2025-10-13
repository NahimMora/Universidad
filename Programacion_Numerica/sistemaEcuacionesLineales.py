import numpy as np

"""
Bloque 2 – Programación
— Diseñar programas para:
• Determinar normas de VECTORES. L
• Determinar normas de MATRICES. X
• Resolver SISTEMAS LINEALES mediante los métodos de:
 Gauss  Gauss – Jordan
 Crout  Cholesky
 Gauss-Seidel  Jacobi
 Relajamiento  Mejoramiento Iterativo
 SOR
Nota: Para los métodos directos programar estrategias de pivoteo:
• Pivoteo Simple
• Pivoteo Parcial
• Pivoteo Total
"""

def normaVector(V):
    max = 0
    
    for i in range (len(V)):
        if abs(V[i]) > max:
            max = V[i]
    return max

def rotarFilas(A, i1, i2):
    n = A.shape(1)
    
    for j in range (n):
        aux = A[i1][j]
        A[i1][j] = A[i2][j]
        A[i2][j] = aux
    return A

def pivoteoSimple(A, k):
    if A[k][k] != 0 and k < A.shape(0):
        return A
    
    A = rotarFilas(A, k, k+1)
    
    return pivoteoSimple(A, k+1)

def sustitucionRegresiva(G):
    n = G.shape(0)
    x = [0] * n 
    
    for i in range (n-1, -1, -1):
        suma = 0
        for j in range(i+1, n):
            suma += G[i][j] * x[j]
        x[i] = (G[i][-1] - suma) / G[i][i]

def sustitucionDiagonal(G):
    n = G.shape(0)
    x = [0] * n 
    

def gauss(A, b):
    
    n = A.shape[0]
    G = np.hstack((A, b))
        
    for k in range (1, n-1):
        G = pivoteoSimple(G, k)
        
        for i in range (k+1, n):
            m = G[i, k] / G[k, k]
            G[i, k] = 0
            
            for j in range (k+1, n+1):
                G[i, j] = G[i, j] - m* G[k, j]
    return sustitucionRegresiva(G)

def gaussJordan(A, b):
    
    G = np.hstack((A, b))
    n = A.shape(0)
    
    for k in range (1, n):
        G = pivoteoSimple(G, k)
        
        for i in range (1, n):
            if i != k:
                m = G[i][k]/G[k][k]
                
                for j in range (k, n+1):
                    G[i][j] = G[i][j] - m* G[k][j]
    return sustitucionDiagonal(G)
    