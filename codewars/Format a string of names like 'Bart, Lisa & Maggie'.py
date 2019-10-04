def namelist(names):
    arr = []
    for x in names:
        arr.append(x['name'])
    ln = len(arr)
    if ln < 2:
        return ''.join(arr)
    elif ln == 2:
        a = ' & '.join(arr)
        return a
    else:
        a = ' & '.join(arr[-2:])
        b = ', '.join(arr[:-2])
        val = f'{b}, {a}'
        return val