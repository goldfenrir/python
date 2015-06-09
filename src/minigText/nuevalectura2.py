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

def imprimir_resto(clase, puesto, descrip, req):
    #lineaTotal = filter(lambda x: x in string.printable, lineaTotal)
    archEscritura.write(clase)
    archEscritura.write(",")
    blobPuesto = TextBlob(puesto.decode('utf-8'))
    blobDescrip = TextBlob(descrip.decode('utf-8'))
    blobReq = TextBlob(req.decode('utf8', 'ignore'))
    wordsPuesto = blobPuesto.words
    wordsDescrip = blobDescrip.words
    wordsReq = blobReq.words
    
    for wordP in wordsPuesto:
        nword = strip_accents(wordP)
        exclude = set(string.punctuation)
        nword = ''.join(ch for ch in nword if ch not in exclude)
        nword = nword.lower()
        nword = filter(lambda x: x in string.printable, nword)
        archEscritura.write(nword)
        archEscritura.write(" ")
    archEscritura.write(",")
    stemmer = SnowballStemmer("spanish")
    cad = ""
    for wordD in wordsDescrip:
        nwordD = strip_accents(wordD)
        exclude = set(string.punctuation)
        nwordD = ''.join(ch for ch in nwordD if ch not in exclude)
        nwordD = filter(lambda x: x in string.printable, nwordD)
        if nwordD not in (stopwords.words('spanish')):#Elimnimar Stop words
            w=Word(nwordD)        
        #comentarios.append(w)
            word2= stemmer.stem(w.lower())
            archEscritura.write(word2)
            archEscritura.write(" ")
    archEscritura.write(",")
    lista = []
    for wordP in wordsReq:
        nwordP = strip_accents(wordP)
        exclude = set(string.punctuation)
        nwordP = ''.join(ch for ch in nwordP if ch not in exclude)
        nwordP = filter(lambda x:x in string.printable, nwordP)
        if nwordP not in (stopwords.words('spanish')):
            w=Word(nwordP)
            word3 = stemmer.stem(w.lower())
            if word3 not in lista:
                lista.append(word3)
    for pal in lista:
        archEscritura.write(pal)
        archEscritura.write(" ")
    archEscritura.write("\n")
                    
        
    
archLectura=open('TA_Registros_etiquetados.csv','r')#Leer archivo

archEscritura= open('Resultados1.txt', 'w')
archEscritura.write("%1. Title: BT database\n")
archEscritura.write("@DATA\n")
lineas=archLectura.readlines()
#print "Read Line: %s" % (lineas)
lineaTotal=""
ind = 0
clase = " "
trabajo = " "
primero = 1
descrip = " "
count = 0
while count < len(lineas):
    lineaClase = ""
    lineaPuesto = " "
    lineaDescrip = " "
    lineaReq = " "
    restoLinea = lineas[count].split('"')
    puesto = restoLinea[0].split(',')
    lineaClase = puesto[1]
    lineaPuesto = puesto[3]
    aux = ""
    for lin in restoLinea[1:]:
        aux += lin
    if '","' not in lineas[count]:
        lineaDescrip +=aux
        count += 1
        while '","' not in lineas[count]:
            lineaDescrip += lineas[count]
            count += 1
        lineaDescrip += lineas[count][:lineas[count].find('","')]
        lineaReq += lineas[count][lineas[count].find('","')+2:]
    else: 
        lineaDescrip += aux[:aux.find('","')]
        lineaReq += aux[aux.find('","')+2:]     
    count += 1
    while 1:
        if count == len(lineas): 
            break
        restoLinea = lineas[count].split('"')
        puesto = restoLinea[0].split(',')
        if len(puesto)>=3 and puesto[0][0].isdigit() and puesto[1][0].isdigit() and puesto[2][0].isdigit():
        #imprimir
            imprimir_resto(lineaClase, lineaPuesto, lineaDescrip, lineaReq)
            break
        else:
            lineaReq += lineas[count]
            count += 1
            
imprimir_resto(lineaClase, lineaPuesto, lineaDescrip, lineaReq)