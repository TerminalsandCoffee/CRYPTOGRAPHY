def decrypt_caesar_cipher(ciphertext, shift):
    return ''.join(
        chr((ord(char) - shift - ord('A')) % 26 + ord('A')) if char.isupper()
        else chr((ord(char) - shift - ord('a')) % 26 + ord('a')) if char.islower()
        else char
        for char in ciphertext
    )

def decrypt_all_shifts(ciphertext):
    return {
        shift: decrypt_caesar_cipher(ciphertext, shift)
        for shift in range(26)
    }

# Given cipher text
ciphertext = "enterthegivencipherhere"

# Get all possible decryptions
possible_decryptions = decrypt_all_shifts(ciphertext)

# Display all possible decrypted texts
print(possible_decryptions)
