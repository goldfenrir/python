#!/usr/bin/python -i
"""Para ejecutar el programa por terminal
https://pypi.python.org/pypi/nltk
"""

from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords

import math
import string

archLectura=open('TA_Registros_etiquetados1.csv','r')#Leer archivo

#archBag=open('Bag of words.txt','w')#Archivo de salida
#archRepBin=open('Representacion binaria.txt','w')
#archFreq=open('Frecuencia.txt','w')
#archTF_IDF=open('TF_IDF.txt','w')
#archDoc=open('Documentos.txt','w')

lineas=archLectura.readlines()
#print "Read Line: %s" % (lineas)

lineaTotal=""
for linea in lineas:
    lineaTotal+=linea
blob=TextBlob(lineaTotal.decode('utf-8'))
words=blob.words
#print words
comentarios=[]
for word in words:    
    if word not in (stopwords.words('spanish')):#Elimnimar Stop words
        w=Word(word)        
        comentarios.append(w.lower())

print "Nuevo: %s " % (comentarios)
#print stopwords.words('spanish')
