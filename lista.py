
from calendar import c


chain = "aabcccdeeee"
print(chain)
patron = []
longitud = len(chain)
print("La longitud de la cadena es:", longitud)
i=0
while i != longitud:
    print(f"index {i}:", chain[i])
    try:
        repeticion=0
        if chain[i] == chain[i+1]:
            print("Encontre una coincidencia:",chain[i])
            patron.append(chain[i])
            print("El patron:", patron)
            repeticion = i+1
            print("Numero de repetciones:", repeticion)
        else:
            patron.append(chain[i])  
    except:
        patron.append(chain[i])
        print("El patron:", patron)
        print("termine de iterar")
    i = i+1
print("El patron el una lista es:", patron)




    
   
# for elemento in chain:
#     if chain[0] == chain[1]:
#         patron=patron.append[chain[0]]
#         print(patron)
        