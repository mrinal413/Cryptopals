from base64 import b64decode

from Crypto.Cipher import AES

def AES_ECB_DECRYPT(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)


with open("chall7.txt") as file:
    data = file.read()

ciphertext = b64decode(data)
plaintext = AES_ECB_DECRYPT(b'YELLOW SUBMARINE', ciphertext)

print(plaintext)
