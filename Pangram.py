def check_pangram(text):
    text = text.upper()
    alfabet = [chr(a) for a in range(ord("A"),ord("Z")+1)]
    for a in text:
        if a in alfabet:
            alfabet.remove(a)
    return False if alfabet else True

if __name__ == '__main__':
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"

