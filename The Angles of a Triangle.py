from math import acos, degrees
def checkio(a, b, c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        alfa = round(degrees(acos((b*b+c*c-a*a)/(2*b*c))))
        beta = round(degrees(acos((a*a+c*c-b*b)/(2*a*c))))
        gama = 180 - alfa - beta
    else:
        alfa = beta = gama = 0
    result = [alfa, beta, gama]
    result.sort()
    return result

if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

