def solution(args):
    total_items = range(len(args))
    count = 0

    for i in total_items:
        curr_num = args[i]
        next_num = args[i + 1]
        if curr_num + 1 == next_num:
            count+=1
        else:
            if count >= 3:
                print(f"{args[i - count]}-{args[i]}")
            elif count < 3:
                print(f"{args[i:i + count]}")
            else:
                print(f"single item {args[i]}")
            count = 0

'''
is this num == next?
count++

is next == after?
count++
etc.

until not - break and then:
take index of 'this num' to index of 'this num + count' and stringify '{this num}-{this num + count}'
continue on from 'this num + count + 1'




'''



solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"