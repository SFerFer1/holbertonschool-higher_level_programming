#!/usr/bin/python3
def roman_to_int(roman_string):
    Valores = {'I': 1, 'V': 5,'X': 10,'L': 50}
    mayor = 0
    letraM = ""
    resta = 0
    suma = 0
    total = 0
    


    for i in roman_string:
        if Valores[i] > mayor:
            mayor = Valores[i]
            letraM = ""
            letraM += i
    if letraM == "":
        for j in roman_string:
            total += Valores[j]
        return total



    for n in roman_string:
        resta += Valores[n]
        if n == letraM:
            break
    
    for t in range(len(roman_string) - 1, -1, -1):
        if n == letraM:
            break
        suma += Valores[roman_string[t]]
        

    total = ((Valores[letraM] - resta) + suma)
    return total