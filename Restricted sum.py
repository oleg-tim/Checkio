def checkio(data):
    if data:
        a = data.pop() + checkio(data)
    else:
        a = 0
    return a
