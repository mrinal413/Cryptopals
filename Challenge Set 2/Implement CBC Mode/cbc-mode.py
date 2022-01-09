from binascii import  a2b_base64
import string
from Crypto.Cipher import AES

def fixed_xor(a, b):
    return bytes([x^y for (x,y) in zip(a, b)])

def pkcs7_padding(s, p):
    b = p-(len(s))
    nstr=""
    for i in range(p):
        if i < len(s):
            nstr = nstr+s[i]
        else:
            nstr = nstr + chr(92) +'x' + str(b).zfill(2)
    return nstr
 
def bytes_to_str(byte_list: bytes) -> str:
    return "".join(filter(lambda x: x in string.printable, "".join(map(chr, byte_list))))

def aes_in_ecb_mode(ciphertext, key, encrypt):
    cipher = AES.new(key, AES.MODE_ECB)
    if encrypt:
        return cipher.encrypt(ciphertext)
    else:
        return cipher.decrypt(ciphertext)

def cbc_mode(byte_string: bytes, 
             key: bytes, 
             initialization_vector: bytes, 
             encrypt: bool = True) -> bytes:
    if encrypt: 
        previous_block = initialization_vector
        cipher_text = b''
        for i in range(0, len(byte_string), len(key)):
            plain_text = fixed_xor(pkcs7_padding(byte_string[i: i + len(key)], len(key)),
                                   previous_block)
            previous_block = aes_in_ecb_mode(plain_text, key, encrypt=True)
            cipher_text += previous_block
        return cipher_text
    else:
        previous_block = initialization_vector
        plain_text = b''
        for i in range(0, len(byte_string), len(key)):
            cipher_text = byte_string[i: i + len(key)]
            plain_text += fixed_xor(aes_in_ecb_mode(cipher_text, key, encrypt=False), previous_block)
            previous_block = cipher_text
        return plain_text

byte_string = b''.join([a2b_base64(line.strip()) for line in open("chall10.txt").readlines()])
for line in bytes_to_str(cbc_mode(byte_string, b'YELLOW SUBMARINE', b'\x00'*16, encrypt=False)).split("\n")[:10]:
    print(line)
