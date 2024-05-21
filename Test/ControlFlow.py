
def filter_prime_numbers(numbers):
    prime_numbers = []
    for i in numbers:
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count += 1
        if count == 2:
            prime_numbers.append(i)
    print("New list is of prime numbers is: ", prime_numbers)


n = int(input("Enter number of elements you want to add in the list: "))
numbers_list = []
print("Enter elements to add into the list: ")
for i in range(0,n):
    value = int(input())
    numbers_list.append(value)

filter_prime_numbers(numbers_list)


