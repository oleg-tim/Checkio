'''
Вам необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв. 
Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa". 
Последняя подстрока является самой длинной, что и делает ее ответом.

Входные данные: Строка.
Выходные данные: Целое число. 
'''

def long_repeat(line):
    win = 0
    for i in range(len(line), 0, -1):
        if list(filter(lambda x: line.count(x*i), set(line))):
            win = i
            break
    return win

def long_repeat_2(line):
    maxi = 0
    calc = 0
    current = ''
    for letter in line:
        if letter == current:
            calc += 1
        else:
            calc = 1
        maxi = max(maxi, calc)
        current = letter
    return maxi

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
