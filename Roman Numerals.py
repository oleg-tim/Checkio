def checkio(data):
    number = ''
    slovar = [ [1000,'M'],
               [900,'CM'], [500,'D'],[400,'CD'], [100,'C'],
               [90,'XC'], [50,'L'], [40,'XL'], [10,'X'],
               [9,'IX'], [5,'V'], [4,'IV'], [1,'I'] ]
    while data != 0:
        for key, value in slovar:
            if key <= data:
                data -= key
                number += value
                break
    return number

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
