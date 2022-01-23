def xor(a, b):
    return bytes([x^y for (x,y) in zip(a,b)])

def score(ciphertext):
    s = []
    for i in range(65,122):
        keystream = (i.to_bytes(1,byteorder='big'))*len(ciphertext)

        res = xor(ct,keystream)
        freq = 0
        for j in res:
            if chr(j).isalpha():
                freq += 1
        
        a = [freq, chr(i)]
        s.append(a)
    return s

ct = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
l = score(ct)

max=0
key = ' '
for i in range(57):
    if l[i][0]>max:
        max = l[i][0]
        key = l[i][1]
print("Message: ", xor(ct,((ord(key)).to_bytes(1,byteorder='big'))*len(ct)), "\nKey: ",key)





