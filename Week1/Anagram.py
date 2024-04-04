
"""Write a Python function that checks if two given strings are anagrams of each other
(contain the same characters in any order)"""


def is_anagram(a,b):
    if sorted(a) == sorted(b):
        print("The strings are anagram")
    else:
        print("The strings are not anagram")


first_string = input("Enter first string ")
second_string = input("Enter second string ")
is_anagram(first_string, second_string)
