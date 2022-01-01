def xor(a, b):
    return bytes([x^y for (x,y) in zip(a, b)])

def single_byte_xor(ciphertext):
    best = None
    for i in range(2**8): # for every possible ascii chars
        candidate_key = i.to_bytes(1, byteorder='big')
        keystream = candidate_key*len(ciphertext)
        candidate_message = xor(ciphertext, keystream)
        score = sum([ x in char_list for x in candidate_message])
        if best == None or score > best['score']:
            best = {"message": candidate_message, 'score': score, 'key': candidate_key}
    return best


char_list = list(range(97, 122)) + [32]
ciphertext = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
result = single_byte_xor(ciphertext)

print('message:', result['message'])
