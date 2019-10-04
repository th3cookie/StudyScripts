def unique_in_order(iterable):
    rni = range(0,len(iterable))
    arr = []
    for i in rni:
        # print(i)
        prev = i - 1
        if prev != -1:
            if len(iterable) == 1:
                arr.append(iterable[i])
                break
            elif iterable[i] == iterable[prev]:
                pass
            else:
                arr.append(iterable[i])
        else:
            arr.append(iterable[i])
    return arr