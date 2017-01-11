import types
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if isinstance(args[0], (types.GeneratorType, filter, set)):
        args = list(args[0])
    if len(args) == 1 and isinstance(args[0], (tuple, list, str, range, filter)):
        args = args[0]
    if not key:
        min = args[0]
        for a in args:
            if a < min:
                min = a
        return min
    else:
        min = key(args[0])
        min_return = args[0]
        for a in args:
            if key(a) < min:
                min = key(a)
                min_return = a
        return min_return

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if isinstance(args[0], (types.GeneratorType, filter, set)):
        args = list(args[0])
    if len(args) == 1 and isinstance(args[0], (tuple, list, str, range, filter)):
        args = args[0]
    if not key:
        max = args[0]
        for a in args:
            if a > max:
                max = a
        return max
    else:
        max = key(args[0])
        max_return = args[0]
        for a in args:
            if key(a) > max:
                max = key(a)
                max_return = a
        return max_return

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

