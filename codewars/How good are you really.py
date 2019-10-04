def better_than_average(class_points, your_points):
    sum = 0
    count = 0
    for i in class_points:
        sum += i
        count += 1
    average = (sum + your_points) / (count + 1)
    if your_points > average:
        return True
    else:
        return False