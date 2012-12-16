#!/usr/bin/python
#-*- coding: utf-8-*-

def luhn(nombre):
    l = []
    for i,  n in enumerate(reversed([int(x) for x in list(str(nombre))])) :
        if i % 2 == 0:
            l.append(n)
        else:
            l.append((2*n)/10 + (2*n)%10)
    return sum(l)

def isValide(n):
    return luhn(n) % 10 == 0

def cle(n):
    c = (10 - luhn(10*n) % 10) % 10
    return 10*n + c


n = 3101997
print n
n = cle(n)
print n
print isValide(n)

n = 6541897
print n
print isValide(n)
