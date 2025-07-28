#vigenere brute forcer
#technically written by myself but HEAVILY assisted by madness' help pdf

#this one is not normalised
def indexCoincidence(cText1): #measures likelihood that any two characters in a text are the same
    #I = 26 Σi=A^Z fi(fi-1)/N(N-1)
    #f = frequency
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #takes a list so below sorts out list
    cText = ""
    for i in range(len(cText1)):
        cText = cText + cText1[i]
        cText = cText.lower()
    count = [0] * 26 #initialies the counting thing so there's a space for each letter
    for chr in cText1:
        index = alphabet.index(chr)
        count[index] += 1 #counts frequency
    n = 0 #the fi*fi-1 
    total = 0 
    for i in range(26):
        n += count[i]*(count[i]-1)
        total += count[i]
    return n/(total*(total-1))

'''
ioc stuff: normal english is around 0.065
random text is 0.0385

polyalphabetic:
n alphabet used = every n characters all use different alphabets/an alphabet gets reused every n characters
0.04 = around 8 alphabets used

'''

def normalisedIndexCoincidence(cText):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cText = cText.replace(" ", "")
    count = [0] * 26
    for chr in cText:
        index = alphabet.index(chr)
        count[index] += 1 
    n = 0
    total = 0 
    for i in range(26):
        n += count[i]*(count[i]-1)
        total += count[i]
    return (26*n)/(total*(total-1)) #the only difference is here (x26)

def createPeriodsList(ioclist, ioc, period, periodlist): #it takes the periods, does them chronologically, and then creates a list based on the order
    if len(ioclist) == 0:
        ioclist.append(ioc)
        periodlist.append(period)
        return 1
    else:
        for i in ioclist:
            if i < ioc:
                index = ioclist.index(i)
                ioclist.insert(index, ioc)
                periodlist.insert(index, period)
                return 1
        ioclist.append(ioc)
        periodlist.append(period)
        return 1

def findPeriod(cText, maxKeyLength): #uses not normalised
    cText = cText.replace(" ", "")
    keyLength = 0 #or period size
    iocList = []
    possiblePeriods = []
    for q in range(maxKeyLength):
        keyLength += 1
        totalSlices = []
        for j in range(keyLength):
            totalSlices.append([])
        for i in range(len(cText)):
            totalSlices[i%keyLength].append(cText[i])
        totalIoc = 0
        for k in totalSlices:
            totalIoc += indexCoincidence(k)
        averageIoc = totalIoc / keyLength
        createPeriodsList(iocList, averageIoc, keyLength, possiblePeriods)
    print(possiblePeriods)
    return possiblePeriods

def decryptVigenere(cText, key):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cText = cText.lower()
    cText = cText.replace(" ", "")
    #ciphertext = 1 long string of lowercase letters
    pText = ""
    for i in range(len(cText)):
        cTextIndex = alphabet.index(cText[i])
        keyIndex = alphabet.index(key[i % len(key)])
        pTextIndex = (cTextIndex - keyIndex) % 26
        pText = pText + alphabet[pTextIndex]
    return pText

def dictionaryAttack(cText, maxKeyLength):
    cText = cText.lower()
    cText = cText.replace(" ", "")
    words = open('files/words.txt', "r") #txt file has been edited and cut!
    words = words.read().splitlines() 
    #if you want non-word keys then go make another function!
    periods = findPeriod(cText, maxKeyLength)
    for j in periods:
        for i in words:
            if len(i) == j:
                print(i)
                pText = decryptVigenere(cText, i)
                currentIoc = indexCoincidence(pText)
                if currentIoc > 0.05:
                    print(pText, i)
                if currentIoc > 0.06:
                    return pText, i 
        
def main():
    ciphertext = input("enter ciphertext: ")    
    print(dictionaryAttack(ciphertext, 8))


def indexCheck():
    text = input("enter text: ")
    text = text.replace(" ", "")
    text = text.lower()
    print(indexCoincidence(text))
