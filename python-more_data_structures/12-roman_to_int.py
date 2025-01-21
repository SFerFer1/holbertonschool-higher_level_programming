#!/usr/bin/python3
def roman_to_int(roman_string):
    Valores = {'I': 1, 'V': 5,'X': 10,'L': 50}
    mayor = 0
    letraM = ""
    resta = 0
    suma = 0
    total = 0
    t = len(roman_string)
    for i in roman_string:
        if Valores[i] > mayor:
            mayor = Valores[i]
            letraM = ""
            letraM += i
    
    for n in roman_string:
        resta += Valores[i]
        if n == letraM:
            break
    
    while t > 0:
        suma += Valores[t]
        if n == letraM:
            break
    total = ((Valores[letraM] - resta) + suma)
    return total