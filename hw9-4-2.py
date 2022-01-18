# Author: ATN 1/14/22

def products(numbers, value):
    for i, v in enumerate(numbers):
        numbers[i] = v * value
        v *= value
    return numbers


print(products([2, 4, 5], 7))
