VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    razdelitel = " .,:;?!"
    text = text.upper()
    newtext = ""
    for i in text:
        if i in razdelitel:
            newtext += " "
        else:
            newtext += i
    mass = newtext.split()

    count = 0
    for word in mass:
        if len(word)>1:
            fl = True
            glas = 0
            for simbol in word:
                if simbol in VOWELS:
                    if glas == 1:
                        fl = False
                        break
                    glas = 1
                else:
                    if simbol in CONSONANTS:
                        if glas == 2:
                            fl = False
                            break
                        glas = 2
                    else:
                        fl = False
                        break
            if fl:
                count += 1
    return count

if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

