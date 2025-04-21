#* Programa que determina la suma mayor de dos datos seguidos
#* Suma todos los datos de la lista en parejas, y retorna la suma mayor
def suma_mayor(x):
    s = 0
    for i in range(1, len(x)):
        if(x[i] + x[i-1]) > s:
            s = x[i] + x[i-1]
    return s
