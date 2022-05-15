# Sample solution for Coding Quest 2022 day 8
# Paul Baumgarten 2022
# codingquest.io

# Vigenère_cipher

import requests

def encode(secret_key, char_set, clear_text):
    cipher_text = ""
    for i in range(len(clear_text)):
        clear_letter = clear_text[i]
        key_letter = secret_key[(i) % len(secret_key)]
        if char_set.find(key_letter) >= 0 and char_set.find(clear_letter)>= 0: # If in character set
            cipher_text += char_set[ (char_set.index(clear_letter) + char_set.index(key_letter) + 1) % len(char_set) ]
        else: # Not in character set, just copy across as is
            cipher_text += clear_letter
    return cipher_text

def decode(secret_key, char_set, cipher_text):
    clear_text = ""
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
        key_letter = secret_key[(i) % len(secret_key)]
        if char_set.find(key_letter) >= 0 and char_set.find(letter) >= 0: # If in character set
            clear_text += char_set[ (char_set.index(letter) - char_set.index(key_letter) - 1) % len(char_set) ]
        else: # Not in character set, just copy across as is
            clear_text += letter
    return clear_text

# Example 1
print(encode("SECRET", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "WE COME IN PEACE"))
print(decode("SECRET", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "PJ UTGX LF JXFFW"))

# Example 2
char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"
print(decode("With great power comes great responsibility", char_set, "lfwwrsvbvMbmIEnK:wDjutpzoxfwowypDDHxB(uwqB8jMA;"))

# Main task
response = requests.get("https://codingquest.io/api/puzzledata?puzzle=8")
cipher_text = response.text
secret_key = "Roads? Where We're Going, We Don't Need Roads."
print(decode(secret_key, char_set, cipher_text))
