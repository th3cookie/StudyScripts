def presses(phrase):
    key_one = ['1']
    key_two = ['a', 'b', 'c', '2']
    key_three = ['d','e','f','3']
    key_four = ['g','h','i','4']
    key_five = ['j', 'k', 'l', '5']
    key_six = ['m', 'n', 'o', '6']
    key_seven = ['p', 'q', 'r', 's', '7']
    key_eigth = ['t', 'u', 'v', '8']
    key_nine = ['w', 'x', 'y', 'z', '9']
    key_zero = [' ', '0']
    key_star = ['*']
    key_hash = ['#']

    sum = 0
    new = phrase.lower()
    for letter in new:
        if letter in key_one:
            sum += key_one.index(letter) + 1
        elif letter in key_two:
            sum += key_two.index(letter) + 1
        elif letter in key_three:
            sum += key_three.index(letter) + 1
        elif letter in key_four:
            sum += key_four.index(letter) + 1
        elif letter in key_five:
            sum += key_five.index(letter) + 1
        elif letter in key_six:
            sum += key_six.index(letter) + 1
        elif letter in key_seven:
            sum += key_seven.index(letter) + 1
        elif letter in key_eigth:
            sum += key_eigth.index(letter) + 1
        elif letter in key_nine:
            sum += key_nine.index(letter) + 1
        elif letter in key_zero:
            sum += key_zero.index(letter) + 1
        elif letter in key_star:
            sum += key_star.index(letter) + 1
        elif letter in key_hash:
            sum += key_hash.index(letter) + 1
    return sum