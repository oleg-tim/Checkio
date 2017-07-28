def checkio(text):
    import re
    sim_max = ''
    sim_max_kol = 0

    text = text.lower()
    find_simvols = re.findall('[a-z]', text)
    unic_simvols = set(find_simvols)
    for i in unic_simvols:
        kol_sim = len(re.findall(i, text))
        if kol_sim > sim_max_kol:
            sim_max_kol = kol_sim
            sim_max = i
        elif kol_sim == sim_max_kol:
            if i < sim_max:
                sim_max_kol = kol_sim
                sim_max = i
    return sim_max

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
