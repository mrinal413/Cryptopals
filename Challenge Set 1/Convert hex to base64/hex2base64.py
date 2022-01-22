from base64 import b64encode, b64decode

def b64TOHex(S):
    return b64decode(S.encode()).hex()

def Hex2b64(S):
    return b64encode(bytes.fromhex(S)).decode()

S1 = input("Enter hex string: ")
print("Base64 encoded string is: ", Hex2b64(S1))
S2 = input("Enter base64 encoded string: ")
print("Hex code:", b64TOHex(S2))
