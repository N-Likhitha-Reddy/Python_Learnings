
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")