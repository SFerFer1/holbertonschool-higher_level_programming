#!/usr/bin/python3
def roman_to_int(roman_string):
    Valores = {'I': 1, 'V': 5,'X': 10,'L': 50,'C': 100 }
    total = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and Valores[roman_string[i]] < Valores[roman_string[i]]:
            total += Valores[roman_string[i]]
        else:
            total -= Valores[roman_string[i]]
        return total

    