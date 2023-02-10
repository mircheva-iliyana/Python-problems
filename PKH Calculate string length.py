# Write a program to calculate the length of a string

def calculate_length(s):
    count = 0
    for letter in s:
        count += 1

    return count


print(calculate_length('Count me'))

