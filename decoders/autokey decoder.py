#autokey! it's like if vigenere jumped off a cliff

#log our key as a letter list
def createKey():
    #takes an encrypt key as an input
    keyLength = int(input("how many letters is the key: "))
    e_key = []
    for i in range(keyLength):
        e_key.append(str((input("letter: "))).lower())
    return e_key

def decryptAutokey(cText, key):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cText = cText.lower()
    cText = cText.replace(" ", "")

    pText = ""
    for i in range(len(cText)):
        cTextIndex = alphabet.index(cText[i])
        keyIndex = alphabet.index(key[i])
        pTextIndex = (cTextIndex - keyIndex) % 26
        pText = pText + alphabet[pTextIndex]
        key.append(alphabet[pTextIndex])
    return pText

def main():
    key = createKey()
    ciphertext = input("Enter ciphertext: ")
    print(decryptAutokey(ciphertext, key))

main()

#this one is difficult... bruteforcing this would be nice
#ofc brute forcing vigenere would be much more useful
