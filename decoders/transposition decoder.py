#transposition decoder

def createKey():
    #takes an encrypt key as an input
    columns = int(input("how many numbers is in the key: "))
    e_key = []
    for i in range(columns):
        e_key.append(int((input("number: "))))
    return e_key


def decryptTransposition(cText, e_key):
    cText = cText.replace(" ", "") #remove spaces in ciphertext
    while len(cText) % len(e_key) != 0:
        cText = cText + "X"

    pText = "" #plaintext
    cTextBlock = [] #ciphertext in correct columns

    for i in range(len(e_key)): #number of columns (lists in cTextBlock)
        column = []
        cTextBlock.append(column)

    count = 0 #counts which letter we're on in ciphertext LMAO
    for l in range(int(len(cText)/len(e_key))): #number of rows #l would count how many rows
        for m in range(len(e_key)): #m will go from 0-6 and repeat this number of row times: keep track of which column we are in
            cTextBlock[m].append(cText[count])
            count = count + 1
        #2d array where each mini list is a list of the letters and it's size of keythis.pictures = [];

    for j in range(len(cTextBlock[0])): #number of rows
        for k in range(len(e_key)): #6
            pText = pText + cTextBlock[e_key[k]-1][int(j)] #first one is number of columns which is key size, second one is how far down the key we are
    return pText


def main():
    ciphertext = str(input("input ciphertext: "))
    encryptKey = createKey()
    print(decryptTransposition(ciphertext, encryptKey).lower())

main()