from binascii import  a2b_base64
import string
from Crypto.Cipher import AES

def fixed_xor(a, b):
    return bytes([x^y for (x,y) in zip(a, b)])

def pkcs7_padding(s, p): #adds required padding to a given text 
    b = p-(len(s))
    nstr=""
    for i in range(p):
        if i < len(s):
            nstr = nstr+s[i]
        else:
            nstr = nstr + chr(92) +'x' + str(b).zfill(2)
    return nstr
 
def bytes_to_str(byte_list: bytes): # To convert the decrypted text in a proper readable string format
    return "".join(filter(lambda x: x in string.printable, "".join(map(chr, byte_list))))

def AES_ECB_DECRYPT(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

def cbc_mode(byte_string, key, IV):
    previous_block = IV
    plain_text = b''
    for i in range(0, len(byte_string), len(key)):
        cipher_text = byte_string[i: i + len(key)]
        plain_text += fixed_xor(AES_ECB_DECRYPT(cipher_text, key), previous_block)
        previous_block = cipher_text
    return plain_text

byte_string = b''.join([a2b_base64(line.strip()) for line in open("chall10.txt").readlines()])
for line in bytes_to_str(cbc_mode(byte_string, b'YELLOW SUBMARINE', b'\x00'*16)).split("\n")[:10]:
    print(line)
