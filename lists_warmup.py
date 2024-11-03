numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = everything but 2
numbers[3:4] = 1
5 in numbers = 9
7 in numbers = an error would occur (outside of the list)
"3" in numbers = an error would occur (string value when it's expecting an int)
numbers + [6, 5, 3] = [3, 1, 4, ..., 2, 6, 5, 3]
"""

numbers[0] = "Ten"
numbers[6] = 1
print(numbers[2:])
if 9 in numbers:
    print("Yep, 9 is definitely in 'numbers'")
else:
    print("No, 9 is 100% not in 'numbers'")
print(numbers)