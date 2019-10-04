def to_weird_case(string):
    final = ''
    arr = string.split()
    for i in arr[0:]:
        new = []
        for x in range(len(i)):
            if x%2 == 0:
                b = i[x].upper()
                new.append(b)
            else:
                b = i[x].lower()
                new.append(b)
        final += f"{''.join(new)} "
    return final.strip()