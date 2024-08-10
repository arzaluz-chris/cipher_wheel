import numpy as np

# Función para encontrar el inverso modular de una matriz en un campo Z_m
def mod_inv_matrix(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)  # Inverso del determinante módulo m
    matrix_modulus_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_modulus_inv

# Función para convertir texto a números
def text_to_numbers(text, alphabet):
    return [alphabet.index(char) for char in text]

# Función para convertir números a texto
def numbers_to_text(numbers, alphabet):
    return ''.join([alphabet[num] for num in numbers])

# Función para cifrar usando Hill Cipher
def hill_cipher_encrypt(plain_text, key_matrix, alphabet):
    plain_numbers = text_to_numbers(plain_text, alphabet)
    plain_matrix = np.array(plain_numbers).reshape(-1, key_matrix.shape[0])
    cipher_matrix = np.dot(plain_matrix, key_matrix) % len(alphabet)
    cipher_text = numbers_to_text(cipher_matrix.flatten(), alphabet)
    return cipher_text

# Función para descifrar usando Hill Cipher
def hill_cipher_decrypt(cipher_text, key_matrix, alphabet):
    inverse_key_matrix = mod_inv_matrix(key_matrix, len(alphabet))
    cipher_numbers = text_to_numbers(cipher_text, alphabet)
    cipher_matrix = np.array(cipher_numbers).reshape(-1, key_matrix.shape[0])
    decrypted_matrix = np.dot(cipher_matrix, inverse_key_matrix) % len(alphabet)
    decrypted_text = numbers_to_text(decrypted_matrix.flatten(), alphabet)
    return decrypted_text

# Alfabeto para la cipher wheel
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Matriz de clave (3x3) para cifrado de Hill
key_matrix = np.array([[6, 24, 1],
                       [13, 16, 10],
                       [20, 17, 15]])

# Texto en claro
plain_text = 'HELLO'.upper()

# Asegurando que el texto tenga la longitud adecuada (múltiplo de 3)
while len(plain_text) % key_matrix.shape[0] != 0:
    plain_text += 'X'

# Cifrado
cipher_text = hill_cipher_encrypt(plain_text, key_matrix, alphabet)
print(f'Texto cifrado: {cipher_text}')

# Descifrado
decrypted_text = hill_cipher_decrypt(cipher_text, key_matrix, alphabet)
print(f'Texto descifrado: {decrypted_text}')

# Mostrar la matriz inversa utilizada para descifrar
inverse_key_matrix = mod_inv_matrix(key_matrix, len(alphabet))
print(f'Matriz inversa de la clave:\n{inverse_key_matrix}')
