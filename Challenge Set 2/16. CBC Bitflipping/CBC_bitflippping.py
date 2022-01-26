from Crypto.Cipher import AES, pad, unpad, xor
from os import urandom

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


def cbc_mode(text, key, IV, encrypt):
    if encrypt:
        en = AES.new(key, AES.mode_CBC, iv)
        text = text.replace(';','X').replace('=','X')
        new_text = "comment1=cooking%20MCs;userdata=" + text + ";comment2=%20like%20a%20pound%20of%20bacon"
        new_text = pkcs7_padding(new_text, 16)
        ciphertext = en.encrypt(new_text)
        return ciphertext
    else: #decrypt
        d = AES.new(key, AES.mode_CBC, iv)
        plaintext = d.decrypt(text)
        return plaintext

string = ";admin=true;"
key = urandom(16)
iv = urandom(16)

ct = cbc_mode(string, key, iv, True)

c0 = chr(ord(ct[0])^ord('X')^ord(';'))
c6 = chr(ord(ct[6])^ord('X')^ord('='))
c11 = chr(ord(ct[11])^ord('X')^ord(';'))

ct = c0 + ct[1:6]+c6+ct[7:11]+c11+ct[12:]

pt = cbc_mode(ct,key,iv,False)

if ";admin=true;" in pt:
    print("True")
else:
    print("FALSE")
