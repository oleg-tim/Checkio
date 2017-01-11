def checkio(required, operations):

    def dlina(mas):
        rez = 0
        for elem in mas:
            if elem[0] + elem[1] != 0:
                rez += elem[1]-elem[0]+1
        return rez

    def cut(enum):
        x, y = operations[enum-1]
        for a in operations[:enum-1]:
            xa, ya = a
            if xa <= x <= ya or xa <= y <= ya:
                merge = a+operations[enum-1]
                x, y = min(merge), max(merge)
                operations[operations.index(a)] = [0, 0]
                operations[enum-1] = [x, y]
            else:
                if x <= xa <= y and x <= ya <= y:
                    operations[operations.index(a)] = [0, 0]
                if xa <= x <= ya and xa <= y <= ya:
                    operations[enum] = [0, 0]
                    break
        return dlina(operations[:enum])

    for enum, element in enumerate(operations, 1):
        if cut(enum) >= required:
            return enum
    return -1


if __name__ == '__main__':
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
