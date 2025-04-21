#* Programa que dada una lista retorna todas lass palabras que sean similares.
#* Iguales cuenta tods las letras de una palabra y comprueba si la otra tiene esa misma cantidad
def iguales(x,y):
  if len(x) != len(y):
    return("Las palabras son de diferente longitud")
  for i in range(len(x)):
    r = 0
    s = 0
    for j in range(len(x)):
      s += (x[i] == x[j])
    for j in range(len(y)):
      r += (x[i] == y[j])
    if r != s:
      return False
  return True

#* Este programa junta todas las palabras iguales en un arreglo, y luego los 
#* Une en un gran arreglo
def cadena_iguales(x):
    s = []
    for i in range(len(x)):
        p = []
        for j in range(len(x)):
            if iguales(x[i],x[j]) == True:
                p.append(x[j])
        if p not in s:
            s.append(p)
    return s

#* Dado que la funcion anterior retornaba palabras unicas tambien,
#* Esta funcion elimina listas de una sola palabra.
def quita_unicos(x):
    s = []
    for i in range(len(x)):
        if (len(x[i]) > 1):
            s.append(x[i])
    return s

#* Esta funcion une las dos anteriores para crear una lista de listas de palabras que sean iguales.
def palabras_iguales(x):
    return quita_unicos(cadena_iguales(x))
