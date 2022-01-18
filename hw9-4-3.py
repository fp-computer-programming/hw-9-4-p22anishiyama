# Author: ATN 1/18/22

def count_e(value):
    counter = 0
    for letter in value:
        if letter == "e":
            counter += 1
    
    return counter

print(count_e("enterprise"))
