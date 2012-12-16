#!/usr/bin/python
#-*- coding: utf-8-*-

def luhn(nombre):
    listeChiffres = [int(chiffres) for chiffres in list(str(nombre))]
    listeChiffres.reverse()
    
    listeLuhn = []
    index = 0
    for chiffres in listeChiffres:
        if index% 2 == 0:
            listeLuhn.insert(index, chiffres)
        else:
            doubleChiffre = chiffres * 2
            sommeDouble = 0
            if len(str(doubleChiffre)) > 1:
                a = list(str(doubleChiffre))
                sommeDouble = sum([int(el) for el in a])
                listeLuhn.insert(index, sommeDouble)
            else:
                listeLuhn.insert(index, doubleChiffre)
        index += 1

    listeLuhn.reverse()
    return "".join(str(el) for el in listeLuhn)

def isValide(nombre):
    lisNombre = [int(el) for el in list(str(nombre))]
    sommeNombre = sum(lisNombre)
    
    return sommeNombre % 10 == 0

def sommeNombre(nombre):
    lisNombre = [int(el) for el in list(str(nombre))]
    return sum(lisNombre)
    

nbr = 54321 
nbrLuhn = int(luhn(nbr))

valide = isValide(nbrLuhn)

if not valide:
    print "Nombre non valide ! Recherche d'un chiffre de contrôle."
    nbrLuhn = int(luhn(nbr))
    valide = isValide(nbrLuhn)
    nbr = int(str(nbr) + "0")
    somNombre =sommeNombre(nbr)
    x = 10 -(somNombre % 10) 
    print "Chiffre de contrôle trouvé : %d" % x
    nbr = int(str(nbr).replace(str(nbr)[-1], str(x)))
    print "Le nouveau nombre qui marche est :%d " % (nbr)
else:
    print "Nombre valide ! Pas besoin de chiffre de contrôle."
