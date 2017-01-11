def checkio(expression):
    skobki = {"[": "]", "{": "}", "(": ")"}
    open_skobki = []
    flag = True

    for simbol in expression:
        if simbol in skobki.keys():
            open_skobki.append(simbol)
        if simbol in skobki.values():
            if open_skobki:
                a = open_skobki.pop()
                if simbol != skobki[a]:
                    flag = False
                    break
            else:
                flag = False
                break
    return flag and (not open_skobki)

if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

