
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

# Function to encode a word
def encode_word(word):
    if len(word) >= 3:
        first_letter = word[0]
        remaining = word[1:]
        new_word = "xyz" + remaining + first_letter + "abc"
        return new_word
    else:
        return word[::-1]  # reverse the word

# Function to decode a word
def decode_word(word):
    if len(word) >= 3:
        # Remove first 3 and last 3 letters
        middle = word[3:-3]
        last_letter = middle[-1]
        remaining = middle[:-1]
        original_word = last_letter + remaining
        return original_word
    else:
        return word[::-1]  # reverse the word

# Ask user what they want to do
choice = input("Do you want to encode or decode? ").lower()

# Ask for message
message = input("Enter your message: ")

# Split message into words
words = message.split()

# Empty list to store result
result = []

# Loop through words and encode/decode
for word in words:
    if choice == "encode":
        result.append(encode_word(word))
    elif choice == "decode":
        result.append(decode_word(word))
    else:
        print("Invalid choice! Please type encode or decode.")
        break

# Show final result
print("Result:", ' '.join(result))
