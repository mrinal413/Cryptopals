def xor(a, b):
    return bytes([x^y for (x,y) in zip(a, b)])

def score(ciphertext):
    s = []
    for i in range(65,122):
        keystream = (i.to_bytes(1,byteorder='big'))*len(ciphertext)

        res = xor(ciphertext,keystream)
        freq = 0
        for j in res:
            if chr(j).isalpha():
                freq += 1
        
        a = [freq, chr(i)]
        s.append(a)
    return s

with open('chall4.txt') as file:
    ciphertext_list = [
        bytes.fromhex(line.strip())
        for line in file
    ]

for i in range(len(ciphertext_list)):
    l = score(ciphertext_list[i])
    max=0
    key = ' '
    for i in range(57):
        if l[i][0]>max:
            max = l[i][0]
            key = l[i][1]
    print("Message: ", xor(ciphertext_list[i],((ord(key)).to_bytes(1,byteorder='big'))*len(ciphertext_list[i])), "\nKey: ",key)

