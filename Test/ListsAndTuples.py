
def sort_integer(tuples_list):
    def sort_key(item):
        return item[1]
    sorted_list = sorted(tuples_list, key=sort_key, reverse=True)
    return [item[0] for item in sorted_list]


def user_data():
    tuples_list = []
    n = int(input("Enter number of tuples: "))
    for i in range(0,n):
        string = input(f"Enter a string for tuple {i}: ")
        integer = int(input(f"Enter an integer for tuple {i}: "))
        tuples_list.append((string, integer))
    return tuples_list


data = user_data()
sorted_strings = sort_integer(data)
print("Sorted strings are: ", sorted_strings)