# Author: ATN 1/18/22

def sum_nums(first, second):
    total = 0
    if first<second:
        total = first + second
        return total
    elif first == second:
        return first

print(sum_nums(2, 3))
print(sum_nums(4, 4))
