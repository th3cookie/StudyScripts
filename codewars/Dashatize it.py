def dashatize(num):
    arr = []
    stringy = str(num)
    if stringy != 'None':
        stringy = stringy.strip('-')
    if stringy == 'None':
        return 'None'
    elif stringy == '0':
        return '0'
    for i in stringy:
        if int(i) % 2 == 0:
            arr.append(i)
        elif int(i) == 0:
            arr.append(i)
        else:
            arr.append(f'-{i}-')
        v = ''.join(arr).strip('-')
    return v.replace('--', '-')