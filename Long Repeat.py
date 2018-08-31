def long_repeat(line):
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
    print('"Run" is good. How is "Check"?')
