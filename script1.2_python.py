#! /usr/vin/env python3

import os
import os.path
import glob
#from pathlib import Path
from sys import argv
from pathlib import Path

script, dirpath = argv



if(os.path.isdir(dirpath)):	#Comprovem si el directori existeix

	contingut = os.listdir(dirpath)	#Guardem tots els directoris i fitxers del directori passat com a argument
	
	

#s=bin(os.stat(dirpath).st_mode&0o777)
#print(s)

#while (os.path.isdir(dirpath)):
#	glob.glob(dirpath), os.walk	
#	print("dir:")


#fitxer=input("Introdueix: ")

	
#llista=[]
#for linia in linias:
#	p,*S,u=linia		#per separar la llista
#	p=p[1:10]		#per eliminar el primer caracter de la llis
#	#print(p)
#	#print(u)
#	tupla = (p, u)
#	llista.append(tupla)	#ajuntar totes les la tupla a la llista
#
#llista.pop(0)		#per treure la 1ra linia
#<<print (llista)
