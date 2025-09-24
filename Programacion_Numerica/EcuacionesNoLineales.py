def biseccion(f, a, b, e):
    
    if f(a)*f(b) > 0:
        return None
    
    c = (a+b)/2
    
    while abs(f(c)) > e:
        
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
            
        c = (a+b)/2
    return c

def regula_falsi(f, a, b, e):
    
    if f(a)*f(b) > 0:
        return None
    
    c = (a*f(b) - b*f(a))/(f(b)-f(a))
    
    while abs(f(c)) > e:
        
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

f = lambda x: x**3 - x - 2
raiz = regula_falsi_modificada(f, 1, 2, 1e-6)
print("Raiz: ", raiz)

print("Raiz: ", raiz)