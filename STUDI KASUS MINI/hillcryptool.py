import numpy as np

# fungsi enkripsi Hill Cipher
def hill_encrypt(text, key_matrix):
    text = text.replace(" ", "").upper()
    while len(text) % 2 != 0:
        text += 'X'
    
    result = ""
    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i]) - 65], [ord(text[i+1]) - 65]])
        enc = np.dot(key_matrix, pair) % 26
        result += chr(int(enc[0][0]) + 65)
        result += chr(int(enc[1][0]) + 65)
    return result

# kunci sesuai di CrypTool: [[3,3],[2,5]]
key = np.array([[3,3],
                [2,5]])

plaintext = "HELLOWORLD"
cipher = hill_encrypt(plaintext, key)

print("Plaintext :", plaintext)
print("Ciphertext:", cipher)
