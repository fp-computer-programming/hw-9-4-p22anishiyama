# Author: ATN 1/14/22

import enum


def products(numbers, value):
    for i, v in enumerate(numbers):
        try:
            v * value
        except:
            return "An error occurred"
    return numbers


print(products([2, 4, 5], 7))
