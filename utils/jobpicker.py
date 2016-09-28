#Yikai Wang and Farhan Haque

import random

def importCSV(fileName):
    inStream = open(fileName, 'r')
    lines = inStream.readlines()
    inStream.close()
    return lines

def cleanUp(L):
    for w in range(len(L)):
        L[w] = L[w].strip()
        L[w] = L[w].strip( "\n" )
        L[w] = L[w].strip( "\r" )
        if ('"' in L[w][0]):
            L[w] = L[w].split( '"' )[1:]
            L[w][1] = L[w][1][1:]
        else:
            L[w] = L[w].split( ',' )
    return L

def convertToList(fileName):
    L = cleanUp(importCSV(fileName))
    return L

def randChooser(D):
    D = D[1:len(D)-1]
    x = random.randrange(998)
    sumLast = 0
    for i in D:
        sumLast = sumNow = sumLast + (float(i[1])*10)
        if ( x < sumNow ):
            return i[0]