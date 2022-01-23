def fixed_xor(a,b):
    return (bytes([x^y for (x,y) in zip(a,b)])).hex()

a = input("Enter hex string: ")
b = input("Enter hex string: ")

res = fixed_xor(bytes.fromhex(a),bytes.fromhex(b))

print(res)
