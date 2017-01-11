def checkio(data):
    data.sort()
    len_data = len(data)
    if (len_data+1) % 2 == 0:
        rez = data[int((len_data+1)/2)-1]
    else:
        rez = (data[int(len_data/2)-1]+data[int(len_data/2)])/2
    return rez

if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
