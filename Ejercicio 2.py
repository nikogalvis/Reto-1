#* Palindrome sin slicing, el programa compara que los 
#* Valores de las esquinas sean iguales
#* Y lo hace sucesivamente hasta llegar el valor del medio
def palindrome(x):
    for i in range(len(x)//2):
        if (x[i] != x[len(x)-1-i]):
            return False
    return True
