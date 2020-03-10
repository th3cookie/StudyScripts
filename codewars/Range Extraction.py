def solution(args):
    total_items = range(len(args))
    count = 0
    new_arr = []
    for i in total_items:
        curr_num = args[i]
        try:
            next_num = args[i + 1]
        except IndexError:
            next_num = None
        if curr_num + 1 == next_num:
            count+=1
        else:
            if count >= 2:
                new_arr.append(f"{args[i - count]}-{args[i]}")
            elif count == 1:
                new_arr.append(f"{args[i-1]}")
                new_arr.append(f"{args[i]}")
            else:
                new_arr.append(f"{args[i]}")
            count = 0

    return ",".join(new_arr)


solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"