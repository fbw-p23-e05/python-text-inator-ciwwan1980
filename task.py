

# word = input("Enter the word: ")

# if word[-1].isalpha() and word[-1].lower() not in "aeiou":
#     inator = "inator"
# else:
#     inator = "-inator"

# length = len(word)
# output = f'{word} {inator} {length}000'
# print(output)

#---------------Another solution"

# word=input("Enter the word: ")

# def function():
#     if word[-1].isalpha() and word[-1].lower() not in "aeiou":
#         return f"{word}-inator {len(word) * 1000}"
#     else:
#         return f"{word} inator {len(word) * 1000}"

# result = function()
# print(result)

word = input("Enter the word: ")

if word[-1].isalpha():
    suffix = ' inator' if word[-1].lower() not in 'aeiou' else ' -inator'
    modified_word = f"{word}{suffix} {len(word) * 1000}"
    print(modified_word)
else:
    print("Invalid input.")
