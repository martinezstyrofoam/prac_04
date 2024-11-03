def number_sort():
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
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


number_sort()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
in_username = input("What is your username? ")
check_usernames = usernames.count(in_username)
if check_usernames > 0: # solution was instead "if username in usernames:". More graceful. Do  instead for future code.
    print("Access granted!")
else:
    print("Access denied!")
