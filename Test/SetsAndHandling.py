
text1 = open("ExampleDataOne", "r")
text2 = open("ExampleDataTwo", "r")

for line in text1:
    line = line.strip()
    line = line.lower()
    words1 = line.split(" ")

for line in text2:
    line = line.strip()
    line = line.lower()
    words2 = line.split(" ")

#PENDING - The program should output these common words in a new file called "common_words.txt".

