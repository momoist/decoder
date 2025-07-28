#vigenere decoder

#log our key as a letter list
def createKey():
    #takes an encrypt key as an input
    keyLength = int(input("how many letters is the key: "))
    e_key = []
    for i in range(keyLength):
        e_key.append(str((input("letter: "))).lower())
    return e_key

def decryptVigenere(cText, key, buffer):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cText = cText.lower()
    cText = cText.replace(" ", "")
    #ciphertext = 1 long string of lowercase letters
    pText = ""
    for i in range(len(cText)):
        cTextIndex = alphabet.index(cText[i])
        keyIndex = alphabet.index(key[i % len(key)])
        pTextIndex = ((cTextIndex - keyIndex) % 26 ) - buffer
        pText = pText + alphabet[pTextIndex]
    return pText

#using a crib like isla
def findKey(cText, crib):
    crib = str(crib)
    crib = crib.replace(" ", "")
    crib = crib.lower()
    longCribLength = len(cText) // len(crib)
    longCrib = crib * longCribLength 
    for i in range(len(cText) - len(longCrib)):
        longCrib = longCrib + crib[i % len(crib)]
    return decryptVigenere(cText, longCrib)

def encryptVigenere(pText, key):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    pText = pText.lower()
    pText = pText.replace(" ", "")
    cText = ""
    for i in range(len(pText)):
        pTextIndex = alphabet.index(pText[i])
        keyIndex = alphabet.index(key[i % len(key)])
        cTextIndex = (pTextIndex + keyIndex) % 26
        cText = cText + alphabet[cTextIndex]
    return cText




#running the program:
def decrypt():
    key = createKey()
    ciphertext = input("input ciphertext: ")
    buffer = int(input("Is A=0 or A=1?"))
    print(decryptVigenere(ciphertext, key, buffer))

def key():
    ciphertext = input("input ciphertext: ")
    crib = input("input crib: ")
    print(findKey(ciphertext, crib))

def encrypt():
    key = createKey()
    plaintext = input("input plaintext: ")
    print(encryptVigenere(plaintext, key))

decrypt()