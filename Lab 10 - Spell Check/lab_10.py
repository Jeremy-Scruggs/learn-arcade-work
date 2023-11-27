import re


# Function to split a line into words
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# Reading the dictionary into an array
with open("dictionary.txt", "r") as dict_file:
    dictionary_list = [word.strip().upper() for word in dict_file]

print("--- Linear Search ---")

with open("AliceInWonderLand200.txt", "r") as alice_file:
    line_number = 0
    for line in alice_file:
        line_number += 1

        # Separating the words using the function above
        word_list = split_line(line)

        for word in word_list:
            if word.upper() not in dictionary_list:
                print(f"Line {line_number} possible misspelled word: {word}")

print("\n--- Binary Search ---")

with open("AliceInWonderLand200.txt", "r") as alice_file:
    line_number = 0
    for line in alice_file:
        line_number += 1

        word_list = split_line(line)

        for word in word_list:
            low, high = 0, len(dictionary_list) - 1
            while low <= high:
                mid = (low + high) // 2
                if dictionary_list[mid] == word.upper():
                    break
                elif dictionary_list[mid] < word.upper():
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                print(f"Line {line_number}  possible misspelled word: {word}")
