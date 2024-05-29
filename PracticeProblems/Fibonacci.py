
def fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the position of the Fibonacci number you want to find: "))
try:
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
except ValueError as e:
    print(e)