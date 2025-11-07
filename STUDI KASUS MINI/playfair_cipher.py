# playfair_cipher.py

def generate_key_matrix(key):
    # Hilangkan duplikat huruf dan ganti J dengan I
    key = key.upper().replace("J", "I")
    key_matrix = []
    seen = set()

    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            key_matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Tanpa J
        if char not in seen:
            seen.add(char)
            key_matrix.append(char)

    # Buat matrix 5x5
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == char:
                return i, j
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i + 1 < len(text) else 'X'
        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared

def playfair_encrypt(text, matrix):
    text = prepare_text(text)
    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]
    return ciphertext

def playfair_decrypt(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            plaintext += matrix[row_a][(col_a - 1) % 5]
            plaintext += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += matrix[(row_a - 1) % 5][col_a]
            plaintext += matrix[(row_b - 1) % 5][col_b]
        else:
            plaintext += matrix[row_a][col_b]
            plaintext += matrix[row_b][col_a]
    return plaintext

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def main():
    print("=== PROGRAM PLAYFAIR CIPHER ===")
    key = input("Masukkan kunci: ")
    plaintext = input("Masukkan teks: ")

    matrix = generate_key_matrix(key)
    print("\nMatriks Kunci (5x5):")
    print_matrix(matrix)

    ciphertext = playfair_encrypt(plaintext, matrix)
    decrypted = playfair_decrypt(ciphertext, matrix)

    print("\nHasil Enkripsi :", ciphertext)
    print("Hasil Dekripsi :", decrypted)

    # Simpan hasil ke file
    with open("hasil_playfair.txt", "w") as f:
        f.write("=== HASIL PLAYFAIR CIPHER ===\n")
        f.write(f"Kunci        : {key}\n")
        f.write(f"Teks Asli    : {plaintext}\n")
        f.write(f"Hasil Enkripsi: {ciphertext}\n")
        f.write(f"Hasil Dekripsi: {decrypted}\n")

    print("\nHasil disimpan di file 'hasil_playfair.txt'.")

if __name__ == "__main__":
    main()
