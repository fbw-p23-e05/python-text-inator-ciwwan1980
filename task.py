

# * Concatenates inator to the end if the word ends with a consonant otherwise, concatenate -inator instead.

# * Adds the word length of the original word to the end, supplied with '000'.

word=input("Enter the word: ")


if word and word[-1].isalpha():
    suffix = ' inator' if word[-1].lower() not in 'aeiou' else ' -inator'
    modified_word = f"{word}{suffix} {len(word) * 1000}"
    print(modified_word)
else:
    print("Invalid input.")
