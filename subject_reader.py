"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_data() # Data is returned from func load_data(). In this case, it would be load_data(subject)
    # print(subjects)
    print_subject(subjects)


def print_subject(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students!")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject = []
    for line in input_file:
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject.append(parts) # Subject gets data taken and stored in parts, and added into a list.
    input_file.close()
    return subject # Because this is in a function, return is needed to return data.


main()