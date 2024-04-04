
"""Write a Python function that checks if a given string is a palindrome
 (reads the same forwards and backwards). Ignore spaces, punctuation, and capitalization."""


def is_palindrome(string_value):
    string_value = string_value.lower()
    original_string = ''
    reverse_string = ''
    for i in string_value:
        if i.isalpha():
            original_string = original_string + i
    print("original string is ", original_string)
    for j in string_value[::-1]:
        if j.isalpha():
            reverse_string = reverse_string + j
    print("reversed string is ", reverse_string)
    return original_string == reverse_string


name = input("Enter a string ")
result = is_palindrome(name)
if result:
    print("It is a palindrome")
else:
    print("It is not a palindrome")