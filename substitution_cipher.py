import random
import copy

# Random monoalphabetic substitution cipher
def encrypt(string):
    string = string.lower() # Transforms string to lower caser
    string = list(string)
    encrypted_string =  ""
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_substitution = copy.copy(alphabet)
    random.shuffle(alphabet_substitution)

    for i in range(0, len(string)):
        for j in range(0, len(alphabet)):
            if string[i] == alphabet[j]:
                letter_substitution = alphabet_substitution[j]
                encrypted_string += str(letter_substitution)
    return encrypted_string

text = input("Please input text: ")
encrypted_text = encrypt(text)
print("Encrypted string: {}".format(str(encrypted_text)))