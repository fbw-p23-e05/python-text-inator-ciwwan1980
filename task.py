word = input("Enter the word: ")

if word[-1].isalpha() and word[-1].lower() not in "aeiou":
    inator = "inator"
else:
    inator = "-inator"

length = len(word)
output = f'{word}{inator} {length}000'
print(output)
