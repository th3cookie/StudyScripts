def digitize(n):
    s = str(n)
    return [int(x) for x in s[::-1]]