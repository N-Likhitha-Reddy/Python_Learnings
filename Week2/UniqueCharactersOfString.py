
def unique_characters(input_string):
    unique_chars = []
    seen_chars = []

    for char in input_string:
        if char not in seen_chars:
            unique_chars.append(char)
            seen_chars.append(char)
        elif char in unique_chars:
            unique_chars.remove(char)

    return unique_chars


input_str = input("Enter a string ")
print("Unique characters are ", unique_characters(input_str))


