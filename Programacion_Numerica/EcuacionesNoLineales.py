import math
import sympy as sp

def biseccion(f, a, b, e= 1e-6):
    
    if f(a)*f(b) > 0:
        return None
    
    c = (a+b)/2
    i = 0
    while abs(f(c)) > e:
        i+=1
        print(i, " a: ", a, " b: ", b, " c: ", c, " f(a): ", f(a), " f(c): ", f(c))
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
            
        c = (a+b)/2
    return c

def regula_falsi(f, a, b, e=0.000001):
    
    if f(a)*f(b) > 0:
        return None
    
    c = (a*f(b) - b*f(a))/(f(b)-f(a))
    i=0
    
    while abs(f(c)) > e:
        
        i+=1
        print(i, " a: ", a, " b: ", b, " c: ", c, " f(a): ", f(a), " f(c): ", f(c))
        
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
            
        c = (a*f(b) - b*f(a))/(f(b)-f(a))
    return c

def regula_falsi_modificada(f, a, b, e):
    
    if f(a)*f(b) > 0:
        return None
    
    F, G = f(a), f(b)
    w = F
    
    c = (a*G - b*F)/(G-F)
    
    while abs(f(c)) > e:
        
        if f(a)*f(c) < 0:
            b = c
            G = f(c)
            if w*G > 0:
                F /= 2
        else:
            a = c
            F = f(c)
            if w*F > 0:
                G /= 2
        w = f(c)
        
        c = (a*G - b*F)/(G-F)
    
    return c

def metodo_newton(f, x1, e=1e-6):
    
    x = sp.symbols('x')
    df = sp.diff(f(x), x)
    
    f_func = sp.lambdify(x, f(x), 'numpy')
    df_func = sp.lambdify(x, df, 'numpy')
    
    while True:
        x0 = x1
        x1 = x0 - f_func(x0) / df_func(x0)

        if abs(x1-x0) < e:
            break
    
    return x1

def metodo_secante(f, x0, x1, e=1e-6, max_iter=100):
    for _ in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        if abs(x2 - x1) < e:
            return x2 
        
        x0, x1 = x1, x2
    
    raise ValueError("No convergió en el número máximo de iteraciones")


f = lambda x: math.e**x - x**2 + 1
raiz = regula_falsi(f, -2, 0)
print("Raíz aproximada:", raiz)
