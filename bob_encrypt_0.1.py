my_text = input("Input the text:")
key = int(input("Input key:"))


def encrypt(text):
    encrypt_text = ""
    for x in text:
        if x.isalpha():
            encrypt_text = encrypt_text + chr(ord(x) + key)
        else:
            encrypt_text = encrypt_text + x
    return encrypt_text

print(encrypt(my_text))