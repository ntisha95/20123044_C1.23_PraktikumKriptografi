# Implementasi sederhana Vigenere Cipher

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper()
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext


# Uji coba
plaintext = "HELLO WORLD"
key = "KEY"

ciphertext = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(ciphertext, key)

print("Plaintext :", plaintext)
print("Kunci     :", key)
print("Ciphertext:", ciphertext)
print("Dekripsi  :", decrypted)
