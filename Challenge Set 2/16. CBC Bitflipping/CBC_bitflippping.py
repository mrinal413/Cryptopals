from Crypto.Cipher import AES
from os import urandom

key = urandom(16)
iv = urandom(16)


def pkcs7_padding(s, p):
    b = p-(len(s))
    nstr=""
    for i in range(p):
        if i < len(s):
            nstr = nstr+s[i]
        else:
            nstr = nstr + chr(92) +'x' + str(b).zfill(2)
    return nstr


def CBC_encrypt(payload):
    obj = AES.new(key, AES.MODE_CBC, iv)
    for i in range(len(payload)):
        if payload[i] == ";" or payload[i] == "=":
            payload = payload.replace(payload[i], "?")
    str1 = "comment1=cooking%20MCs;userdata=" + payload + ";comment2=%20like%20a%20pound%20of%20bacon"
    str1 = pkcs7_padding(str1, 16)
    ciphertext = obj.encrypt(str1)
    return ciphertext


def CBC_decrypt(ciphertext):
    obj1 = AES.new(key,AES.MODE_CBC,iv)
    plaintext = obj1.decrypt(ciphertext)
    if ";admin=true;" in plaintext:
        print("True")
    else:
        print("FALSE")


# Exploit using the Bit Flipping Attack!
cipher_list = []
payload = ";admin=true;"
ciphertext = CBC_encrypt(payload)

i = 0
while i*16 <= len(ciphertext):
    cipher_list.append(ciphertext[i*16: 16 + (i*16)])
    i += 1
cipher_list.remove(cipher_list[6])

attack_on_block = cipher_list[1]
list1 = list(attack_on_block)
list1[0] = chr(ord(list1[0]) ^ ord("?") ^ ord(";"))
list1[6] = chr(ord(list1[6]) ^ ord("?") ^ ord("="))
list1[11] = chr(ord(list1[11]) ^ ord("?") ^ ord(";"))
cipher_list[1] = ''.join(list1)
ciphertext = ''.join(cipher_list)

CBC_decrypt(ciphertext)
