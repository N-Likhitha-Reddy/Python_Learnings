
#Write a Python script that generates a random password of a specified length, consisting of uppercase letters, lowercase letters, and digits. Utilize the random module for this task.

import string
import random

length = int(input("Enter length of password you want to create: "))

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

choice_count = int(input("Enter number of choices you want to add: "))
characterList = ""

while choice_count:
    choice = int(input("Pick your choice from above to have those only those characters in your password: "))

    if choice == 1:
        characterList += string.digits
        choice_count -= 1
    elif choice == 2:
        characterList += string.ascii_letters
        choice_count -= 1
    elif choice == 3:
        characterList += string.punctuation
        choice_count -= 1
    elif choice == 4:
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    random_char = random.choice(characterList)
    password.append(random_char)

print("The random password is " + "".join(password))