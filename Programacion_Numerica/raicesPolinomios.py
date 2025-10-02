import math

"""
— Realizar un programa que incorpore procedimientos para:
a) Calcular el valor de un polinomio para un determinado punto.
b) Dividir un polinomio de grado n por otro de la forma a x  b.
c) Dividir un polinomio de grado n por otro de la forma x2 + p x + q
d) Determine las posibles raíces enteras.
e) Determine las posibles raíces racionales.
f) Determine las cotas de las raíces positivas y negativas por distintos métodos.
g) Encontrar raíces reales por el método de Newtos para polinomios.
— Implemente el Método de Bairstow.
— Diseñe casos de pruebas y realice un informe sobre el funcionamiento de los programas.

"""

def calcularValor(P, x):
    suma = 0
    n = len(P)
    
    for i in range(1, n):
        suma += (x**i)*P[i]
        
    return suma

def ruffiniSimple(P, r):
    
    n = len(P)
    b = [P[0]]
    
    for i in range(1, n):
        b.append(P[i] + r*b[-1])
    
    cociente = b[:-1]
    resto = b[-1]
    
    return cociente, resto

def ruffiniDoble(P, Q):
    
    n = len(P)
    r = Q[1]
    s = Q[0]
    
    b = [0]*n
    
    b[0] = P[0]
    b[1] = P[1] + r*b[0]
    
    for i in range(2, n):
        b[i] = P[i] + r*b[i-1] + s*b[i-2]
    
    cociente = b[:-2]
    resto = (b[-2], b[-1])
    
    return cociente, resto

def encontrarDivisores(x):
    
    divisores = []
    
    for i in range(1, abs(x+1)):
        
        if x % i == 0:
            divisores.append(i)
            divisores.append(-i)
    
    return divisores    

def posiblesRaicesEnteras(P):
    
    a0 = [P[0]]
    
    posibles = encontrarDivisores(a0)
    
    return posibles

def posiblesRaicesRacionales(P):
    
    n = len(P)
    
    r = 0
    
    p = encontrarDivisores(P[n])
    q = encontrarDivisores(P[0])
    
    posibles = set()
    
    for i in range(len(p)):
        for j in range(len(q)):
            if q[j] != 0 and math.gcd(int(p[i]), int(q[j])) == 1:
                posibles.append(p[i]/q[j])
    
    return posibles

def datosLagrange(P):
    
    n = len(P)
    
    k = 0
    
    for i in range(n):
        return 

def cotasLagrange(P):
    
    cotas = []
    
    
    for i in range(4):
        return 