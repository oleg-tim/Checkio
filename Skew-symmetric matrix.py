def checkio(matrix):
    dl = len(matrix[0])
    rezult = True
    for x in range(dl):
        for y in range(dl):
            if matrix[x][y] != matrix[y][x]* (-1):
                rezult = False
    return rezult

if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"

