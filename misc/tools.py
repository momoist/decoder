#different mini programs i can use!

#column splitter: splits ciphertext into columns
def columnSplitter(cText, num):
    columns = []
    cText = cText.replace(" ", "")
    for i in range(num):
        columns.append([])
    for i in range(len(cText)):
        columns[i%num].append(cText[i])
    return columns

def columnSplitterRun(text, num): #makes columnSplitter actually usable 
    columns = columnSplitter(text, num)
    columnsList = []
    for i in range(num):
        list = ""
        for j in range(len(columns[num-1])):
            list = list + columns[i][j]
        columnsList.append(list)
    return columnsList

def textHalver(text): #halves it through middle
    text = text.replace(" ", "")
    firstHalf = text[:int(len(text)/2)]
    secondHalf = text[int(len(text)/2):]
    list = [firstHalf, secondHalf]
    return list

def textSplitter(text): #halves it every other
    text = text.replace(" ", "")
    firstHalfLetters = []
    secondHalfLetters = []
    for i in range(len(text)):
        if i % 2 == 0:
            firstHalfLetters.append(text[i])
        if i % 2 == 1:
            secondHalfLetters.append(text[i])
    firstHalf = ""
    secondHalf = ""
    for i in firstHalfLetters:
        firstHalf = firstHalf + i
    for i in secondHalfLetters:
        secondHalf = secondHalf + i
    list = [firstHalf, secondHalf]
    return list

#we need a trigram counter that counts trigrams but also finds the gap between each one
def trigramCounter(text):
    text = text.replace(" ", "")
    trigrams = [text[i:i+3] for i in range(len(text)-2)] #stole this off overflow but it's GENIUS
    trigramsCount = {}
    for i in range(len(trigrams)):
        if trigrams[i] not in trigramsCount:
            trigramsCount.update({trigrams[i]:1})
        else:
            trigramsCount[trigrams[i]] += 1
    #successfully counts the trigrams
    topTrigrams = {}
    for key, value in trigramsCount.items(): #thanks chat gpt
        if value >= 3:
            topTrigrams[key] = value
    return topTrigrams
#work in progress, does not work yet bc it doesn't return top trigrams

#enter trigrams and text, then it will count gaps between each trigrams
def spaceCounter(text, trigrams):
    pass

def stringReverser(text): #reverses text! who could have guessed
    text = text.replace(" ", "")
    reversedString = text[::-1]
    return reversedString

def groupMaker(cText, num): #or space adder depending on how u look at it
    cText.replace(" ", "")
    groups = [cText[i:i + num] for i in range(0, len(cText), num)] #if u want pairs then num = 2
    groups = str(groups)
    return groups

def run(): #edit as needed
    text = input("Enter text: ")
    print(columnSplitterRun(text, 5))

run()