def checkio(array):
    if array:
        b = [y for x, y in enumerate(array) if x % 2 == 0]
        c = array.pop()
        return sum(b)*c
    else:
        return 0

if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"

