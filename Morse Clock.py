def checkio(time_string):
    bin_list = []
    len_bin = 2
    list_time = time_string.split(":")
    for item in list_time:
        item = int(item)
        des = item // 10
        edin = item - des*10

        first_bin = str(bin(int(des)))[2:]
        second_bin = str(bin(int(edin)))[2:]
        if len_bin == 2:
            a = first_bin.rjust(len_bin, "0")
            len_bin += 1
        else:
            a = first_bin.rjust(len_bin, "0")
        b = second_bin.rjust(4, "0")

        bin_list.append(a + " " + b)
    all = " : ".join(bin_list)
    all = all.replace("0", ".")
    all = all.replace("1", "-")
    return all

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"


