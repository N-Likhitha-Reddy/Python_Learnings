
#Create a Python module named utils that contains a function to calculate the factorial of a number.
#Import this module in another script and use the function to calculate the factorial of a given number.

import Utils

number = int(input("Enter number you want to find out factorial for: "))
result = Utils.factorial(number)
print(f"The factorial of {number} is {result}")
