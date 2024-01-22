my_text = input("Input the text:")
key = int(input("Input key:"))


def decrypt(text):
    decrypt_text = ""
    for x in text:
        if x.isalpha():
            decrypt_text = decrypt_text + chr(ord(x) - key)
        else:
            decrypt_text = decrypt_text + x
    return decrypt_text

print(decrypt(my_text))