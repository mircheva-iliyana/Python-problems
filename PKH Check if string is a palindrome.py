# Write a program to check if a string is a palindrome

def is_palindrome(s):
    s = s.lower()
    reversed_s = s[::-1]
    if s == reversed_s:
        return True
    else:
        return False


print(is_palindrome('hjkjh'))

