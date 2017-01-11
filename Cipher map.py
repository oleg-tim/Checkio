def recall_password(cipher_grille, ciphered_password):
    kod = ''
    for rotate in range(0, 4):
        matrix = [["."]*4 for a in range(4)]
        new_cipher_grille = []
        for y in range(0, 4):
            for x in range(0, 4):
                if cipher_grille[y][x] == "X":
                    kod += ciphered_password[y][x]
                    matrix[x][3-y] = "X"
        for line in matrix:
            new_cipher_grille.append("".join(line))
        cipher_grille = new_cipher_grille
    return kod

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

