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


archLectura=open('TA_Registros_etiquetados.csv','r')#Leer archivo

archEscritura= open('Resultados.txt', 'w')
archEscritura.write("%1. Title: BT database\n")
archEscritura.write("@DATA\n")
lineas=archLectura.readlines()
#print "Read Line: %s" % (lineas)

lineaTotal=""
for linea in lineas:
    lineaTotal+=linea
blob=TextBlob(lineaTotal.decode('utf-8'))

#separamos en palabras
words=blob.words
count = 0
primero = 1
while count < len(words) :
    nword = words[count].split(',')
    if len(nword)>2:
        if primero==2:
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
                com = filter(lambda x: x in string.printable, com)
                archEscritura.write(com)
                archEscritura.write(",")
            archEscritura.write("\n")
            
        else:
            primero = 2
        ncomments = []
        ncomments.append(nword[1])
    if len(nword)<2:
        nword = strip_accents(words[count])
        exclude = set(string.punctuation)
        nword = ''.join(ch for ch in nword if ch not in exclude)
        nword = nword.lower()
        ncomments.append(nword)
    count +=1
    
    #print ncomments
#quitamos los stop words
#hacemos un stemming snowball
    