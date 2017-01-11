def checkio(number):
    mass = []

    def delitel(number, list_delitel):
        nonlocal mass
        if number in range(2, 10):
            list_delitel.append(str(number))
            mass.append(list_delitel)
            return True
        else:
            for i in range(2, 10):
                if number % i == 0:
                    if delitel(int(number/i), list_delitel+[str(i)]):
                        break
        return False

    delitel(number, [])
    if mass:
        rezult = min([int("".join(i)) for i in mass])
    else:
        rezult = 0
    return rezult

if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"

