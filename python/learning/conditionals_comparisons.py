###################
### Comparisons ###
###################

1 < 2   # True
0 > 2   # False
2 == 1  # False
2 != 1  # True
3.0 >= 3.0  # True
3.1 <= 3.0  # False
1.1 == "1.1"    # False
1.1 == float("1.1") # True

3.1 <= "this"   # Gives TypeError

"this" == "this"    # True
"this" == "This"    # False
"b" > "a"   # True
"abc" < "b" # True
# The characters are compared one at a time alphabetically to determine which is greater. This concept is used to sort strings alphabetically.

2 in [1, 2, 3]  # True
4 in [1, 2, 3]  # False
2 not in [1, 2, 3]  # False
4 not in [1, 2, 3]  # True

########################
### if - elif - else ###
########################

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

