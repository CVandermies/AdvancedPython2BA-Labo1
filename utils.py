# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from collections import namedtuple

def fact(n):
    if n<0:
        raise ValueError
    if n<2:
        return 1
    else :
        return n*fact(n-1)
print(fact(n))

def roots(a,b,c):
    if a==0:
        print("Veuillez spécifier une équation du second degré")
    else:
        delta = (b**2)-(4*a*c)
        if delta==0:
            return (-b/(2*a))
        elif delta > 0:
            x1 = (-b + delta**0.5)/(2*a)
            x2 = (-b - delta**0.5)/(2*a)
            return (x1,x2)    
        else :
            return ('Impossible')
print(roots(a,b,c))

def ff(x):
    return x
def integrate(function,lower,upper):
    pas = 100000
    h = (upper-lower)/pas
    result = 0
    for i in range(0,n-1):
        result += h * function(lower + h*i)
    return result

    print(x)

            