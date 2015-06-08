#!/usr/bin/python -i
"""Para ejecutar el programa por terminal
https://pypi.python.org/pypi/nltk
"""
from nltk.stem.snowball import SnowballStemmer
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
 	

import math
import string
import unicodedata

def strip_accents(s): 
    #res = s.decode('cp1252');
    return ''.join(c for c in unicodedata.normalize('NFD', s) 
        if unicodedata.category(c) != 'Mn')

archLectura=open('TA_Registros_etiquetados1.csv','r')#Leer archivo
archEscritura= open('Resultados.txt', 'w')
archEscritura.write("%1. Title: BT database\n")
archEscritura.write("@DATA")

lineas=archLectura.readlines()
#print "Read Line: %s" % (lineas)
puesto = lineas[0].split('"')
puesto = puesto[0].split(',')
print puesto[3]
lineaTotal=""
ind = 0
clase = ""
trabajo = ""
for linea in lineas:
    restoLinea = linea.split('"')
    puesto = restoLinea[0].split(',')
    if len(puesto)==5:
        clase = puesto[1]
        trabajo = puesto[3]
        lineaTotal+=clase
        lineaTotal += " "
        lineaTotal+=trabajo
        ind = len(trabajo)
        lineaTotal+= " $ "
        for lin in restoLinea[1:]:
            lineaTotal+=lin
        print lineaTotal
    else:
        lineaTotal+=linea
blob=TextBlob(lineaTotal.decode('utf-8'))

#separamos en palabras
words=blob.words
print words
count = 1
#nword = words[0].split(',')
ncomments = []
ncomments.append(clase)
ncomments.append(trabajo)
aux = trabajo.split(' ')
ind = len(aux) +1
print ind
#ncomments.append(nword[1])
for word in words[ind:]:
    nword = strip_accents(word)
    exclude = set(string.punctuation)
    nword = ''.join(ch for ch in nword if ch not in exclude)
    nword = nword.lower()
    ncomments.append(nword)
    
print ncomments
#quitamos los stop words
#hacemos un stemming snowball
comentarios=[]
stemmer = SnowballStemmer("spanish")
for word in ncomments:    
    if word not in (stopwords.words('spanish')):#Elimnimar Stop words
        w=Word(word)        
        #comentarios.append(w)
        comentarios.append(stemmer.stem(w.lower()))
        
ulist = []
for com in comentarios:
    if com not in ulist:
        ulist.append(com)
         
for com in ulist:
    print com