# Créé par prof, le 28/11/2020
from __future__ import division
from lycee import *
def Nand(a,b):
    c= not(a and b)
    return(c)   #fonction logique essentielle qui permet de construire toutes les autres:
                #Nand(a,a)=Not(a) Nand(Nand(a,a),Nand(b,b))=a Or b
def Xor(a,b):
    if a==b:        #visualiser cette condition simple
        return(0)
    else:
        return(1)

def Halfadder(a,b):
    s=Xor(a,b)
    c=(a and b)
    return(s,c) # on récupère la somme et la retenue

def Adder(a,b,c):   #on retrouve les tables de vérité de Xor
    s=Xor(a,b)      #on calcule en deux fois
    s=Xor(s,c)
    c1=(a and b) or (a and c) or (b and c)
    return(s,c1)    #on peut calculer cette valeur par étapes
def Multiplexor(a,b,sel):
    if sel==0:
        return(a)
    else:
        return(b)
def Demultiplexor(In,sel):
    a=0
    b=0
    if sel==0:
        a=In
    else:
        b=In
    return(a,b)

def And8(a,b):
    c=[0]*8
    for k in range(8):
        c[k]=a[k] and b[k]
    return(c)
def Not8(a):
    c=[0]*8
    for k in rang(8):
        c[k]=not(a[k])
    return(c)
def Or8(a,b):
    c=[0]*8
    for k in rang(8):
        c[k]=(a[k] or b[k])
    return(c)
def Nand8(a,b):
     c=[0]*8
     for k in range(8):
        c[k]=Nand(a[k],b[k])
     return(c)
def Xor8(a,b):
     c=[0]*8
     for k in range(8):
        c[k]=Xor(a[k],b[k])
     return(c)
def Add8(a,b):
    s8=[0]*8                #addition commençant à gauche
    s8[0]=Halfadder(a[0],b[0])[0]
    c=Halfadder(a[0],b[0])[1]
    for k in range(1,8):
        s8[k]=Adder(a[k],b[k],c)[0]
        c=Adder(a[k],b[k],c)[1]
    return(s8)
def Adder8(a,b):            #fonction incorrecte la retenue n'est pas prise
    s=[0]*8                 #en compte
    c=[0]*8                 #addition de gauche à droite
    for k in range(8):      # pour rétablir la disposition naturelle
        s[k]=Xor(a[k],b[k]) # on change k en 7-k
        c[k]= a[k] and b[k]

    return(s)
# TESTS
a=[1,1,0,0,1,1,0,1]
b=[0,1,1,1,0,0,0,1]
print(Add8(a,b))
print(Adder8(a,b))







print(Xor(1,0))
print(Xor(1,1))
print(Halfadder(1,0))
print(Halfadder(1,1))
print(Adder(1,0,1))
print(Adder(1,1,1))
print(Multiplexor(0,1,0))
print(Demultiplexor(1,1))
a=[1,1,0,0,1,1,0,1]
b=[0,1,1,1,0,0,0,1]
print(Add8(a,b))
print(Adder8(a,b))

