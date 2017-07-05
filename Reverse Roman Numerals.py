def reverse_roman(roman_string):
    slovar = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    suma = 0
    for num, i in enumerate(roman_string):
        if num == len(roman_string)-1:
            suma += slovar[i]
        elif slovar[i] >= slovar[roman_string[num+1]]:
            suma += slovar[i]
        else:
            suma -= slovar[i]
    return suma

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
