"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# this example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))

lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
actual_numbers = [int(x) for x in almost_numbers] # Method in subject_reader.py could've worked, need to start list comprehend-ing more
print(actual_numbers)

#greater_than_nine = []
#for x in actual_numbers:
    #if x > 9:
        #greater_than_nine.append(x)
greater_than_nine = [x for x in actual_numbers if x > 9] # translates to "the numbers in list are numbers in actual_numbers if over 9"
print(greater_than_nine)
# to create a string (not list) of the last names for those full names longer than 11 characters
# the result should be: 'Harlem, Hendrix, Lovelace'
#l_names_g_eleven = [x for x in full_names if len(x.split()[1]) > 11]
f_names_g_eleven = [x.split()[1] for x in full_names if len(x) > 11]
print(", ".join(sorted(f_names_g_eleven)))
