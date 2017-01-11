def checkio(number):
    p = 1
    for a in str(number):
        b = int(a)
        if b:
            p *= b
    return p

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

