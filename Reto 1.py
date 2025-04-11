# Calculadora Primitiva, esta toma dos valores reales, un simbolo, y los opera.
def calculadora(a,b,x):
    if(x == "+"):
        return (a+b)
    if(x == "-"):
        return (a-b)
    if(x == "*"):
        return (a*b)
    if(x == "/"):
        return (a/b)

#* Palindrome sin slicing, el programa compara que los 
#* Valores de las esquinas sean iguales
#* Y lo hace sucesivamente hasta llegar el valor del medio
def palindrome(x):
    for i in range(len(x)//2):
        if (x[i] != x[len(x)-1-i]):
            return False
    return True

#* Detector de primos, divide x por todos los numeros hasta la raiz de la misma
#* En caso de que su modulo no sea 0, se retorna como primo
def esprimo(x):
    if (x < 2):
        return False
    for i in range(2,int(x**0.5)+1):
        if (x%i == 0):
            return False
    return True

#* Aplica la funcion anterior a todos los elementos de una lista
def lista_primos(x):
    s =  []
    for i in range(len(x)):
        if(esprimo(x[i])):
            s.append(x[i])
    return s

#* Programa que determina la suma mayor de dos datos seguidos
#* Suma todos los datos de la lista en parejas, y retorna la suma mayor
def suma_mayor(x):
    s = 0
    for i in range(1, len(x)):
        if(x[i] + x[i-1]) > s:
            s = x[i] + x[i-1]
    return s

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

#* Esta funcion une las dos anteriores para crear una lista de palabras que sean iguales.
def palabras_iguales(x):
    return quita_unicos(cadena_iguales(x))