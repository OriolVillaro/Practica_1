#! /usr/bin/env python3

from sys import argv

script, fitxer, qui, perm = argv

with open( fitxer, "r") as f:
	linias=[linia.split() for linia in f]
	
llista=[]
	
for linia in linias:
	
	p,*S,u=linia
	p=p[1:10]
	tupla= (p, u)
	llista.append(tupla)
	
llista.pop(0)	
print (llista)	

