import os
import pyaes

## Abrir arquivo criptografado

file_name = "teste.txt.ransomwaretroll"
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Chave de descriptografia

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover arquivo cript

os.remove(file_name)

# Criar novo arquivo descript

new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
