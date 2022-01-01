plain_text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"

keystream = key*((len(plain_text)//3)+1)

ciphertext = bytes([x^y for (x,y) in zip(plain_text, keystream)])

hexadecimal_string = ciphertext.hex()
print(hexadecimal_string)
