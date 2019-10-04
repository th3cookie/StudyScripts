def high(x):
    var = x.split()
    arr = []
    for i in var:
        sum = 0
        for x in i:
            sum += ord(x) - 96
        print(sum)
        arr.append(sum)
    highest = sorted(arr)
    hi = arr.index(highest[-1])
    return var[hi]