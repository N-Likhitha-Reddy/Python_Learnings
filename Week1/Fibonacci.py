
"""Write a Python function that generates the first n terms of the Fibonacci sequence,
 where each term is the sum of the two preceding terms (starting from 0 and 1)."""


def fibonacci_sequence(num):
    n1, n2 = 0, 1
    count = 0
    while count < num:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    else:
        print("Enter a valid number")


number = int(input("Enter the value of n "))
fibonacci_sequence(number)