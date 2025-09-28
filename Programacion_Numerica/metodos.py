import sympy as sp

def biseccion(f, a, b, e= 1e-6, max_iter= 100):
    
    if f(a)*f(b) > 0:
        return None
    
    c = (a+b)/2
    
    current_iter = 0
    
    while abs(f(c)) > e and max_iter > current_iter:
        
        current_iter +=1
        
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        
        c = (a+b)/2
    return c, current_iter

def regula_falsi(f, a, b, e= 1e-6, max_iter= 100):
    
    if f(a)*f(b) > 0:
        return None
    
    c = (a*f(b) - b*f(a))/(f(b)-f(a))
    
    current_iter = 0
    
    while abs(f(c)) > e and max_iter > current_iter:
        
        current_iter +=1
        
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
            
        c = (a*f(b) - b*f(a))/(f(b)-f(a))
    return c, current_iter

def regula_falsi_modificada(f, a, b, e= 1e-6, max_iter= 100):
    
    if f(a)*f(b) > 0:
        return None
    
    F, G = f(a), f(b)
    w = F
    
    c = (a*G - b*F)/(G-F)
    
    current_iter = 0
    
    while abs(f(c)) > e and max_iter > current_iter:
        
        current_iter +=1
        
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
    return c, current_iter

def newton(f, x1, e= 1e-6, max_iter= 100):
    
    x = sp.symbols('x')
    df = sp.diff(f(x), x)
    
    f_func = sp.lambdify(x, f(x), 'numpy')
    df_func = sp.lambdify(x, df, 'numpy')
    
    current_iter = 0
    
    while True and max_iter > current_iter:
        
        current_iter +=1
        
        x0 = x1
        
        x1 = x0 - f_func(x0) / df_func(x0)

        if abs(x1-x0) < e:
            break
    return x1, current_iter

def secante(f, xn, xn1, e=1e-6, max_iter=100):
    
    current_iter = 0
    
    while True and max_iter > current_iter:
        
        current_iter +=1

        x1n = xn
        xn = xn1
        
        xn1 = xn - f(xn)*(xn - x1n)/(f(xn) - f(x1n))

        if abs(xn1-xn) < e:
            break
    return xn1, current_iter    

# FALTA METODO DE HALLEY