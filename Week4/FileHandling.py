
#Write a Python function that reads a text file line by line, counts the number of occurrences of each word, and returns a dictionary with word counts.

text = open("MyData", "r")

d = dict()

for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])


