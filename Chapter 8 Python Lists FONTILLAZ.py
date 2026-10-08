words = []

with open("romeo.txt", "r") as file:
    for line in file:
        line_words = line.split()

        for word in line_words:
            if word not in words:
                words.append(word)

words.sort()

print(words)