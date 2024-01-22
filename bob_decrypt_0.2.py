My_text = input("Input the text:")
# Key will be under 10
key_1 = int(input("Input first key:"))
key_2 = int(input("Input second key:"))

# Emoji file
dtx = {'🐜':"A", '🐝':"B", '🐈':"C", '🐕':"D", '🐘':"E",
       '🐟':"F", '🦍':"G", '🦉':"H", '🐉':"I", '🦂':"J",
       '🐨':"K", '🦁':"L", '🐁':"M", '🐪':"N", '🐌':"O",
       '🦜':"P", '🐊':"Q", '🦏':"R", '🐍':"S", '🐅':"T",
       '🦄':"U", '🦅':"V", '🦧':"W", '🐞':"X", '🕷️':"Y",
       '🦓':"Z", '🍎':"a", '🍌':"b", '🍭':"c", '🍞':"d",
       '🥐':"e", '🍤':"f", '🍪':"g", '🥞':"h", '🍔':"i",
       '🥗':"j", '🥙':"k", '🍿':"l", '🍠':"m", '🍣':"n",
       '🍩':"o", '🍮':"p", '🍰':"q", '🥨':"r", '🍒':"s",
       '🍘':"t", '🍥':"u", '🥮':"v", '🍷':"w", '🍸':"x",
       '🍺':"y", '🍵':"z", '🚔':"1", '🚖':"2", ' 🚎':"3",
       '🚆':"4", '🚉':"5", '🚑':"6", '🚘':"7",
       '🚚':"8", '🏍️':"9", '💣':"0", '🧭':".", '🎑':"!",
       '👺':":", '✨':",", '🗝️':"'", '☠':'"','🎩':" ",
       '💤':"?", "🦖":"&", "☃️":"/"}

class decrypt:
    # This function encrypt the text
    def decrypt(self,text):

        decrypt_text = ""
        for x in text:
            if text.isalpha(): # only alphabet
                decrypt_text = decrypt_text + chr(ord(x) - key_1 - key_2)
            else:
                decrypt_text = decrypt_text + x
        return decrypt_text


    # This function decrypt into emoji
    def decrypt_to_emoji(self,text):
        decrypt_text = ""
        for x in text:
            if x in dtx:
                decrypt_text = decrypt_text + dtx[x]
            else:
                decrypt_text = decrypt_text + x

        return decrypt_text

decrypt = decrypt()
Out_text = decrypt.decrypt_to_emoji(My_text)
print(decrypt.decrypt(Out_text))