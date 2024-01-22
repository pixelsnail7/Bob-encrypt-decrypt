My_text = input("Input the text:")
# Key will be under 10
key_1 = int(input("Input first key:"))
key_2 = int(input("Input second key:"))

# Emoji file
etx = {"A" : "🐜","B" : "🐝","C" : "🐈",
      "D" : "🐕","E" : "🐘","F" : "🐟",
      "G" : "🦍","H" : "🦉","I" : "🐉",
      "J" : "🦂","K" : "🐨","L" : "🦁",
      "M" : "🐁","N" : "🐪","O" : "🐌",
      "P" : "🦜","Q" : "🐊","R" : "🦏",
      "S" : "🐍","T" : "🐅","U" : "🦄",
      "V" : "🦅","W" : "🦧","X" : "🐞",
      "Y" : "🕷️","Z" : "🦓",
      "a": "🍎", "b": "🍌", "c": "🍭", "d": "🍞",
      "e": "🥐", "f": "🍤", "g": "🍪", "h": "🥞",
      "i": "🍔", "j": "🥗", "k": "🥙", "l": "🍿",
      "m": "🍠", "n": "🍣", "o": "🍩", "p": "🍮",
      "q": "🍰", "r": "🥨", "s": "🍒", "t": "🍘",
      "u": "🍥", "v": "🥮", "w": "🍷", "x": "🍸",
      "y": "🍺", "z": "🍵","1" : "🚔","2":"🚖",
      "3":"🚎","4":"🚆","5":"🚉","6":"🚑",
      "7":"🚘","8":"🚚","9":"🏍️","0":"💣",
      ".":"🧭","!":"🎑",":":"👺",",":"✨",
      "'": "🗝️",'"': "☠"," ":"🎩","/":"☃️",
       "&":"🦖","?":'💤'
      }
class encrypt:
    # This function encrypt the text
    def encrypt(self,text):

        encrypt_text = ""
        for x in text:
            if text.isalpha(): # only alphabet
                encrypt_text = encrypt_text + chr(ord(x) + key_1 + key_2)
            else:
                encrypt_text = encrypt_text + x
        return encrypt_text


    # This function encrypt into emoji
    def encrypt_to_emoji(self,text):
        encrypt_text = ""
        for x in text:
            if x in etx:
                encrypt_text = encrypt_text + etx[x]
            else:
                encrypt_text = encrypt_text + x

        return encrypt_text


encrypt = encrypt()
Out_text = encrypt.encrypt(My_text)
print(encrypt.encrypt_to_emoji(Out_text))

