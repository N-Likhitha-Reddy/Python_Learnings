
def count_characters(string):
    string = string.lower()
    char_count = {}
    for char in string:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


input_string = input("Enter a string: ")
result = count_characters(input_string)
print("Count: ", result)