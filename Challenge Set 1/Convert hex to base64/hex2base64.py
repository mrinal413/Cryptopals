option = int(input("For hex to base64 enter 1 and for base64 to hex enter 2: "))
if option==1:
    # hex -> base64
    s = input("Enter string: ")
    b64 = b64encode(bytes.fromhex(s)).decode()
    print('base64:', b64)
elif option==2:
    # base64 -> hex
    b = input("Enter base64: ")
    s2 = b64decode(b.encode()).hex()
    print('Hex string is:', s2)
