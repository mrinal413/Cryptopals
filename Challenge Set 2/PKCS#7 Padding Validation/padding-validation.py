def pkcs7_padding_validation(s):
    last_byte = s[-1]
    if int(last_byte) > len(s):
        return ValueError("bad padding")
    for i in range(int(last_byte), 0, -1):
        if s[-i] != last_byte:
            raise ValueError("bad padding")
    return s[:-last_byte]

S = input("Enter a padded string: ")
print(pkcs7_padding_validation(S))
