#!/usr/bin/python
#-*- coding: utf-8-*-

def luhn(nombre):
    return sum([(2*n)/10 + (2*n)%10 if i % 2 else n
        for i, n in 
        enumerate(reversed([int(x) for x in list(str(nombre))]))
    ])

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
