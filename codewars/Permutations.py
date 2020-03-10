# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
from itertools import permutations as perm
def permutations(string):
    arr = [''.join(p) for p in perm(string)]
    new_arr = []
    for item in arr:
        if item not in new_arr:
            new_arr.append(item)
    return new_arr

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']