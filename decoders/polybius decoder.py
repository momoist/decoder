def createSquare(): 
    completeAlphabet = "abcdefghijklmnopqrstuvwxyz"
    keywordStr = input("Enter keyword (remove repeating letters beforehand): ")
    alphabet = "" #the alphabet we will then add to our square
    square = []

    if keywordStr != "-1": #no keyword
        alphabet = alphabet + keywordStr 

        lastLetterIndex = completeAlphabet.find(keywordStr[-1]) + 1
        firstLetter = completeAlphabet[lastLetterIndex] #this will be the first letter we add onto alphabet after we remove all the dupes
        for i in completeAlphabet:
            if i in alphabet:
                completeAlphabet = completeAlphabet.replace(i, "")
        firstLetterIndex = completeAlphabet.index(firstLetter)
        alphabet = alphabet + completeAlphabet[firstLetterIndex:]
        alphabet = alphabet + completeAlphabet[:firstLetterIndex] #alphabet is keyword + alphabet after keyword + alphabet before keyword

    else:
        alphabet = completeAlphabet

    removedLetter = str(input("Letter to remove: ")) #removes 1 letter
    alphabet = alphabet.replace(removedLetter, "")

    alphabetIndex = 0
    for k in range(5): 
        line = []
        square.append(line)
        for m in range(5):
            square[k].append(alphabet[alphabetIndex])
            alphabetIndex += 1

    return square

def LettersToNumbers(letters):
    letters = letters.replace(" ", "")
    completeAlphabet = "abcdefghijklmnopqrstuvwxyz"
    lettersLength = int(input("number of different letters: "))
    regularLetters = []
    regularNumbers = []
    numbers = [] #final result
    for i in range (lettersLength):
        regularNumbers.append(i+1)
        regularLetters.append(completeAlphabet[i])
    for i in range(len(letters)):
        index = regularLetters.index(letters[i])
        numbers.append(regularNumbers[index])
    return numbers

def decryptPolybius(cText, square):
    cText = cText.replace(" ", "")
    pText = ""
    cTextCoords = []
    for i in range(int(len(cText)/2)):
        cTextCoords.append(cText[i*2] + cText[(i*2)+1]) #every 2 numbers
    for j in range(len(cTextCoords)):
        coords = cTextCoords[j]
        row = (cTextCoords[j])[0]
        column = (cTextCoords[j])[1]
        pText = pText + square[int(row)-1][int(column)-1]
    return pText

def decryptPolybius2(letters, numbers, square): #this is for the one where first coordinate part was letters and second part was numbers
#letters is misleading as due to a previous function the letters have been transformed into corresponding numbers
    cTextCoords = []
    numbers = numbers.replace(" ", "")
    for i in range(len(letters)):
        coord = str(letters[i]) + str(numbers[i])
        cTextCoords.append(coord)
    pText = ""
    for j in range(len(cTextCoords)):
        row = (cTextCoords[j])[0]
        column = (cTextCoords[j])[1]
        pText = pText + square[int(row)-1][int(column)-1]
    return pText

def main():
    square = createSquare()
    print(square)
    ciphertext = input("Enter ciphertext: ")
    print(decryptPolybius(ciphertext, square))

def sevenB(): #if first coordinate is a letter and second coordinate is a number
    square = createSquare()
    print(square)
    letterCiphertext = input("Enter the letter part of the ciphertext: ")
    numberCiphertext = input("Enter the number part of the ciphertext: ")
    letters = LettersToNumbers(letterCiphertext)
    print(decryptPolybius2(letters, numberCiphertext, square))

def eightB():
    square = createSquare()
    print(square)
    number1 = input("First Half: ")
    number2 = input("Second Half: ")
    print(decryptPolybius2(number1, number2, square))

main()