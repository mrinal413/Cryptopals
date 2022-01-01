def xor(a, b):
    return bytes([x^y for (x,y) in zip(a, b)])

class InvalidMessageException(Exception):
    pass

def single_byte_xor(ciphertext):
    best = {"score": 0}
    for i in range(2**8):
        candidate_key = i.to_bytes(1, byteorder='big')
        candidate_message = xor(ciphertext, candidate_key*len(ciphertext))
        score = sum([ x in char_list for x in candidate_message])
        if score>best['score']:
            best = {"message": candidate_message, 'score': score, 'key': candidate_key}
    
    if best['score'] > 0.7*len(ciphertext):
        return best
    else:
        raise InvalidMessageException('best candidate message is: %s' % best['message'])

with open('chall4.txt') as data_file:
    ciphertext_list = [
        bytes.fromhex(line.strip())
        for line in data_file
    ]

char_list = list(range(97, 122)) + [32] 

message = ""
for (i, ciphertext) in enumerate(ciphertext_list):
    try:
        message = single_byte_xor(ciphertext)['message']
    except InvalidMessageException:
        pass
    else:
        message = message
      
print(message)

