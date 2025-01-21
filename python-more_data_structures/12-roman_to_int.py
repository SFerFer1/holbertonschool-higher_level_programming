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
            letraM = i

    
    if letraM == "" or  mayor == 0:
        for j in roman_string:
            total += Valores[j]
        return total

    for n in roman_string:
        if n == letraM:
            break
        resta += Valores[n]
        
        

    for t in range(len(roman_string) - 1, -1, -1):
        suma += Valores[roman_string[t]]
        if t == letraM:
            break

    if Valores[letraM] == 5 or  Valores[letraM]:
        print(Valores[letraM])
        print(suma)
        print(resta)
    total = ((Valores[letraM] - resta) + suma)
   
    return total