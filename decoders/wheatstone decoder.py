#wheatstone decoder
#replace all backslashes with ] instead

def decrypt6(cText): #bc instead of the usual 5 needles it's 6 so the diamond looks diff
    needle6 = {
        "/||||]":"a",
        "/|||]|":"b",
        "|/|||]":"c",
        "/||]||":"d",
        "|/||]|":"e",
        "||/||]":"f",
        "/|]|||":"g",
        "|/|]||":"h",
        "||/|]|":"i",
        "|||/|]":"j",
        "/]||||":"k",
        "|/]|||":"l",
        "||/]||":"m",
        "|||/]|":"n",
        "||||/]":"o",
        "]/||||":"p",
        "|]/|||":"q",
        "||]/||":"r",
        "|||]/|":"s",
        "||||]/":"t",
        "]|/|||":"u",
        "|]|/||":"v",
        "||]|/|":"w",
        "|||]|/":"x",
        "]||/||":"y",
        "|]||/|":"z",
    }
    cText = cText.replace(" ", "")
    cTextSplit = []
    for i in range(int(len(cText)/6)):
        character = cText[i*6:(i*6)+6]
        cTextSplit.append(character)
    pText = ""
    for j in range(len(cTextSplit)):
        pText = pText + needle6[cTextSplit[j]]
    return pText

def decrypt3(cText):
    needle3 = {
        "/|]":"1",
        "/]|":"2",
        "|/]":"3",
        "]/|":"4",
        "|]/":"5",
        "]|/":"6",
    }

    cText = cText.replace(" ", "")
    cTextSplit = []
    for i in range(int(len(cText)/3)):
        character = cText[i*3:(i*3)+3]
        cTextSplit.append(character)
    pText = ""
    for j in range(len(cTextSplit)):
        pText = pText + needle3[cTextSplit[j]]
    return pText

def main():
    ciphertext = input("Enter ciphertext: ")
    print(decrypt3(ciphertext))

main()
