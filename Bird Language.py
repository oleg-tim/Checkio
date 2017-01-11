VOWELS = "aeiouy"

def translate(phrase):
    phrase_list = list(phrase)
    for nom, bukva in enumerate(phrase_list):
        if bukva:
            if bukva in VOWELS:
                phrase_list[nom+1] = phrase_list[nom+2] = []
            else:
                if bukva == " ":
                    continue
                else:
                    phrase_list[nom+1] = []
    return "".join([i if i else "" for i in phrase_list])

if __name__ == '__main__':
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

