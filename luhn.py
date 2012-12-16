#!/usr/bin/python
#-*- coding: utf-8-*-

def luhn(nombre):
    listeLuhn = []
    for index, chiffre in enumerate(reversed([int(x) for x in list(str(nombre))])) :
        if index % 2 == 0:
            listeLuhn.append(chiffre)
        else:
            d = 2 * chiffre
            n1, n2 = d/10, d%10 
            listeLuhn.append(n1+n2)
    return sum(listeLuhn)

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
