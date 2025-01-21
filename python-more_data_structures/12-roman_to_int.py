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

    
    if all(char == roman_string[0] for char in roman_string):
        for j in roman_string:
            total += Valores[j]
        return total

    for n in roman_string:
        if n == letraM:
            break
        resta += Valores[n]
        
        
    
        for t in reversed(roman_string):
            if t == letraM:
                break
            suma += Valores[t]

   
    total = ((Valores[letraM] - resta) + suma)
   
    return total