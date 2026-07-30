text = input("Enter message: ")
shift = int(input("Enter shift value: "))
encrypt = ""

for ch in text:
    if ch.isalpha():
        if ch.islower():
            encrypt += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            encrypt += chr((ord(ch) - 65 + shift) % 26 + 65)
    else:
        encrypt += ch

print("Encrypted:", encrypt)
decrypt = ""

for ch in encrypt:
    if ch.isalpha():
        if ch.islower():
            decrypt += chr((ord(ch) - 97 - shift) % 26 + 97)
        else:
            decrypt += chr((ord(ch) - 65 - shift) % 26 + 65)
    else:
        decrypt += ch

print("Decrypted:", decrypt)