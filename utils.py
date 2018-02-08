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

print(roots(1,4,3))
            