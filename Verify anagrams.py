def verify_anagrams(first_word, second_word):
    a = ''.join(first_word.split())
    b = ''.join(second_word.split())
    a = list(a.lower())
    b = list(b.lower())
    a.sort()
    b.sort()
    return a == b

if __name__ == '__main__':
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"


