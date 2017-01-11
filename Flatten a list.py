def flat_list(a):
    t = []
    for i in a:
        if isinstance(i, list): t += flat_list(i)
        else: t.append(i)
    return t
