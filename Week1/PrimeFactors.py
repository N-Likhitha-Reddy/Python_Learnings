
"""Write a Python function that finds and returns all the prime factors of a given
positive integer n."""


def prime_factors(n):
    i = 2
    while i <= n:
        if n % i == 0:
            print(i)
            n = n / i
        else:
            i += 1


number = int(input("Enter a number "))
prime_factors(number)