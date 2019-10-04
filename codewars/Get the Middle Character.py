def get_middle(s):
    slen = int(len(s) / 2)
    if len(s) % 2 != 0:
        return s[slen]
    else:
        return s[(slen - 1):(slen + 1)]