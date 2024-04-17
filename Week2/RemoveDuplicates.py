
number_list = []


def remove_duplicates(integer_list):
    final_list = []
    for x in integer_list:
        if x not in final_list:
            final_list.append(x)
    return final_list


def numbers_list():
    n = int(input("Enter number of elements in list "))
    print("Enter elements of list: ")
    for i in range(0, n):
        elements = int(input())
        number_list.append(elements)
    print("Original list is ", number_list)


numbers_list()
print("List after removing duplicates are ", remove_duplicates(number_list))