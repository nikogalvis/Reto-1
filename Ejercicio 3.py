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
