print("Please input 5 numbers!")
numbers = []
number = 5
for number in range(1, 6):
    in_number = int(input("Number: "))
    numbers.append(in_number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The biggest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")