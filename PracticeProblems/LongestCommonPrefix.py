
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

        if not prefix:
            return ""

    return prefix


input_strings = input("Enter a list of strings separated by spaces: ").split()

result = longest_common_prefix(input_strings)
print("Longest common prefix is: ", result)
