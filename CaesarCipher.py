# Function to decrypt the cipher text using Caesar Cipher
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Given cipher text
ciphertext = "enterthegivencipherhere"

# Try different shifts to find the correct decryption
possible_decryptions = {}
for shift in range(1, 26):
    decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
    possible_decryptions[shift] = decrypted_text

# Display all possible decrypted texts
possible_decryptions
