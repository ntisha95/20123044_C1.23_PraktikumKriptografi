def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            if mode == 'encrypt':
                result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            elif mode == 'decrypt':
                result += chr((ord(char) - ord(base) - shift) % 26 + ord(base))
        else:
            result += char
    return result

def main():
    print("=== Program Caesar Cipher ===")

    # LANGSUNG SET teks dan shift di sini:
    text = "informatika"
    shift = 3

    encrypted = caesar_cipher(text, shift, 'encrypt')
    decrypted = caesar_cipher(encrypted, shift, 'decrypt')

    print("\nTeks Asli     :", text)
    print("Hasil Enkripsi:", encrypted)
    print("Hasil Dekripsi:", decrypted)

    with open("hasil_cipher.txt", "w") as f:
        f.write("=== Hasil Caesar Cipher ===\n")
        f.write(f"Teks asli     : {text}\n")
        f.write(f"Hasil enkripsi: {encrypted}\n")
        f.write(f"Hasil dekripsi: {decrypted}\n")

    print("\nHasil disimpan di file 'hasil_cipher.txt'.")

if __name__ == "__main__":
    main()