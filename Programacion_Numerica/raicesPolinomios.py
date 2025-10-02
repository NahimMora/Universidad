import math

#a) Calcular el valor de un polinomio para un determinado punto.
def evaluar_polinomio(P, x):
    resultado = 0
    for i in range(len(P)):
        resultado += P[i] * (x ** i)
    return resultado

#b) Dividir un polinomio de grado n por otro de la forma a x  b.
def ruffiniSimple(P, r):
    
    n = len(P)
    b = [P[0]]
    
    for i in range(1, n):
        b.append(P[i] + r*b[-1])
    
    cociente = b[:-1]
    resto = b[-1]
    
    return cociente, resto

#c) Dividir un polinomio de grado n por otro de la forma x2 + p x + q
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

#d) Determine las posibles raíces enteras.
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

#e) Determine las posibles raíces racionales.
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

#f) Determine las cotas de las raíces positivas y negativas por distintos métodos.
def coeficiente_negativo_max(P):
    
    n = len(P)
    
    k = -1
    A = 0
    
    for i in range(1, n):
        if  P[i] < 0:
            if k == -1: k = i
            
            if A < abs(P[i]): A = abs(P[i])
    return k, A

def cota_superior(P):
    n = len(P)
    
    a0 = P[n-1]
    
    k, A = coeficiente_negativo_max(P)
    
    if k == 0: return 1 + A/a0
    
    return 1 + (A/a0)**(1/k)

def transformar_para_cotas_negativas(P):
    
    n = len(P)
    P1 = []
    
    for i in range(n):
        if i % 2 != 0:
            P1.append(-P[i])
        else:
            P1.append(P[i])

    return P1

def cotasLagrange(P):
    
    c1 = cota_superior(P)
    c2 = 1 / cota_superior(list(reversed(P)))
    c4 = - cota_superior(transformar_para_cotas_negativas(P))
    c3 = - 1 / cota_superior(list(reversed(transformar_para_cotas_negativas(P))))
    
    return c4, c3, c2, c1

def es_polinomio_positivo(Q):
    
    n = len(Q)
    
    esPositivo = True
    
    for i in range(n):
        if Q[i] < 0: esPositivo = False
        
    return esPositivo
        
def evaluar_valores_cociente(P, limite = 100):
    
    num = 0
    
    while True and num < limite:
        
        num += 1    

        Q, R = ruffiniSimple(P, num)
        
        if es_polinomio_positivo(Q):
            break
    
    return num

def cotasLaguerre(P):
    
    c1 = evaluar_valores_cociente(P)
    c2 = 1 / evaluar_valores_cociente(list(reversed(P)))
    c4 = - evaluar_valores_cociente(transformar_para_cotas_negativas(P))
    c3 = - 1 / evaluar_valores_cociente(list(reversed(transformar_para_cotas_negativas(P))))
    
    return c4, c3, c2, c1

def derivar_polinomio(P):
    P1 = []
    for i in range(1, len(P)):
        P1.append(i * P[i])
    return P1

def evaluar_derivadas(P, limite=100):
    for num in range(1, limite+1):
        Q = P[:]
        es_valido = True

        while len(Q) > 0:
            if evaluar_polinomio(Q, num) <= 0:
                es_valido = False
                break
            Q = derivar_polinomio(Q)

        if es_valido:
            return num
    return None


def cotasNewton(P):
    
    c1 = evaluar_derivadas(P)
    c2 = 1 / evaluar_derivadas(list(reversed(P)))
    c4 = - evaluar_derivadas(transformar_para_cotas_negativas(P))
    c3 = - 1 / evaluar_derivadas(list(reversed(transformar_para_cotas_negativas(P))))
    
    return c4, c3, c2, c1

#g) Encontrar raíces reales por el método de Newtos para polinomios.

#— Implemente el Método de Bairstow.


P = [1, 0, -5, 0, 4] 

print(cotasLaguerre(P))
print(cotasNewton(P))

    