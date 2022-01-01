plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"

keystream = key*((len(plaintext)//3)+1)

ciphertext = bytes([x^y for (x,y) in zip(plaintext, keystream)])

hexadecimal_string = ciphertext.hex()

pos = len(plaintext)
for i in range(len(plaintext)):
    if i == '\n':
        pos = i
        break

print(hexadecimal_string[0:pos],"\n",hexadecimal_string[pos+1:])
