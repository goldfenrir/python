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

archEscritura= open('Resultados1.txt', 'w')
archEscritura.write("%1. Title: BT database\n")
archEscritura.write("@DATA\n")
lineas=archLectura.readlines()
#print "Read Line: %s" % (lineas)
lineaTotal=""
ind = 0
clase = ""
trabajo = ""
primero = 1
for linea in lineas:
    restoLinea = linea.split('"')
    puesto = restoLinea[0].split(',')
    
    if len(puesto)==5 and puesto[0].isdigit() and puesto[1].isdigit() and puesto[2].isdigit():
        if primero==2 and len(lineaTotal)>1:
            blob=TextBlob(lineaTotal.decode('utf-8'))
#separamos en palabras
            words=blob.words
            for word in words:
                nword = strip_accents(word)
                exclude = set(string.punctuation)
                nword = ''.join(ch for ch in nword if ch not in exclude)
                ncomments.append(nword)
            comentarios=[]
            stemmer = SnowballStemmer("spanish")
            count = 0
            for word in ncomments:    
                if count < 2:
                    exclude = set(string.punctuation)
                    word = ''.join(ch for ch in word if ch not in exclude)
                    word = word.lower()
                    #word = strip_accents(word)
                    comentarios.append(word)
                else:
                    if word not in (stopwords.words('spanish')):#Elimnimar Stop words
                           
        #comentarios.append(w)
                        exclude = set(string.punctuation)
                        word = ''.join(ch for ch in word if ch not in exclude)
                        word = word.lower()
                        word = strip_accents(word)
                        w=Word(word) 
                        comentarios.append(stemmer.stem(w.lower()))
                count += 1
        
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
        #ncomments.append(nword[1])
        lineaTotal = ""
        
        clase = puesto[1]
        #clase = filter(lambda x: x in string.printable, clase)
        trabajo = puesto[3]
        blob=TextBlob(trabajo.decode('utf-8'))
#separamos en palabras
        words=blob.words
            
        trabajo1 = ""
        for word in words:
            nword = strip_accents(word)
            trabajo1 += nword
            trabajo1 += " "
        #lineaTotal+=clase
        #lineaTotal += " "
        #lineaTotal+=trabajo
        ind = len(trabajo)
        ncomments.append(clase)
        ncomments.append(trabajo1)
        #lineaTotal+= " $ "
        if len(restoLinea) == 2:
            for lin in restoLinea[1:]:
                #print lin
                lineaTotal+=lin
        if len(restoLinea) == 3:
            for lin in restoLinea[1:]:
                print lin
                lineaTotal+=lin
            blob=TextBlob(lineaTotal.decode('utf-8'))
#separamos en palabras
            words=blob.words
            for word in words:
                nword = strip_accents(word)
                exclude = set(string.punctuation)
                nword = ''.join(ch for ch in nword if ch not in exclude)
                ncomments.append(nword)
            comentarios=[]
            stemmer = SnowballStemmer("spanish")
            count = 0
            for word in ncomments:    
                if count < 2:
                    exclude = set(string.punctuation)
                    word = ''.join(ch for ch in word if ch not in exclude)
                    word = word.lower()
                    #word = strip_accents(word)
                    comentarios.append(word)
                else:
                    if word not in (stopwords.words('spanish')):#Elimnimar Stop words
                           
        #comentarios.append(w)
                        exclude = set(string.punctuation)
                        word = ''.join(ch for ch in word if ch not in exclude)
                        word = word.lower()
                        word = strip_accents(word)
                        w=Word(word) 
                        comentarios.append(stemmer.stem(w.lower()))
                count += 1
        
            ulist = []
            for com in comentarios:
                if com not in ulist:
                    ulist.append(com)
         
            for com in ulist:
                com = filter(lambda x: x in string.printable, com)
                archEscritura.write(com)
                archEscritura.write(",")
            archEscritura.write("\n")
            lineaTotal = ""
        #lineaTotal += restoLinea[]
        #print lineaTotal
    else:
        lineaTotal+=linea
        
count = 0
primero = 1


#quitamos los stop words
#hacemos un stemming snowball
