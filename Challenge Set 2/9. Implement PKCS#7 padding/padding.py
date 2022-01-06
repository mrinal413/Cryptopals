def pad(s, p):
    b = p-(len(s))
    nstr=""
    for i in range(p):
        if i < len(s):
            nstr = nstr+s[i]
        else:
            nstr = nstr + chr(92) +'x' + str(b).zfill(2)
    return nstr


s = input("Enter your plaintext: ")
p = int(input("pad length: "))

print(pad(s, p))
