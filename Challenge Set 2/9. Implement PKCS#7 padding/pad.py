from Crypto.Util.Padding import pad

def padding_pkcs7(plaintext, padding_size):
    return pad(plaintext, padding_size)

plaintext = b'Yellow submarine'
padding_size = 20
print(padding_pkcs7(plaintext, padding_size))
