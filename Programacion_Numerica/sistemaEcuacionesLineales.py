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

def pivoteoSimple(A, k):
    if A[k][k] != 0 and k < A.shape(0):
        return A
    
    for i in range (A.shape[0]):
        aux = A[i][k]
        A[i][k] = A[i+1][k]
        A[i+1][k] = aux
    
    return pivoteoSimple(A, k)

def sustitucionRegresiva(G):
    x = [0] * n 
    n = G.shape(0)
    
    for i in range (n-1, -1, -1):
        suma = 0
        for j in range(i+1, n):
            suma += G[i][j] * x[j]
        x[i] = (G[i][-1] - suma) / G[i][i]

def gauss(A, b):
    
    n = A.shape[0]
    G = np.hstack((A, b))
        
    for k in range (1, n-1):
        A = pivoteoSimple(A, k)
        
        for i in range (k+1, n):
            m = G[i, k] / G[k, k]
            G[i, k] = 0
            
            for j in range (k+1, n+1):
                G[i, j] = G[i, j] - m* G[k, j]
    return sustitucionRegresiva(G)