
dictionary1 = {}
dictionary2 = {}


def dict_creator(dict_value, n):
    n = int(input(f"Enter the no. of elements you want in dictionary {n}: "))
    for i in range(n):
        a = input(f"Enter the key and value to be appended in dictionary {n} with space separated: ")
        b = a.split()
        dict_value[b[0]] = b[1]


dict_creator(dictionary1, 1)
dict_creator(dictionary2, 2)

for each_key in dictionary2:
    if each_key in dictionary1:
        new_value = dictionary1[each_key] + dictionary2[each_key]
        print(new_value)
        dictionary1[each_key] = new_value
    else:
        dictionary1[each_key] = dictionary2[each_key]

print("Final dictionary after combining both the dictionaries is ", dictionary1)






