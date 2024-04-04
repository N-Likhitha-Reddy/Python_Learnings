
"""Write a Python function that calculates the sum of all the multiples of 3 or 5
 below a given positive integer n."""


def calculate_sum(num):
    total_sum = 0
    for i in range(num+1):
        if i % 3 == 0 or i % 5 == 0:
            total_sum = total_sum + i
    print(total_sum)


number = int(input("Enter a number "))
calculate_sum(number)
