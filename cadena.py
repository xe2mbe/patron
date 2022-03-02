def LongitudCadena(chain):
    long = len(chain)
    return long

def EncontrarPatron(chain):
    chain = list(chain)
    for i in chain:
        print(i)
        index = print (chain.index)
        return (i, index)
     




cadena = "aabbcc"
print (cadena)
longitud=LongitudCadena (cadena)
print(longitud)

elementos = EncontrarPatron(cadena)
print(elementos)
