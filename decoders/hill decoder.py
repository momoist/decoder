#hill cipher!

#im going to lay out my matrices like this: [[1, 2, 3][4, 5, 6][7, 8, 9]]
#which looks like this: 1 2 3
#                       4 5 6
#                       7 8 9

def createMatrix(num): #does not work with a keyword
    print("the matrix you enter has to already be the inversed version. this will not inverse your encryption matrix for you.")
    matrix = []
    for i in range(num):
        row = []
        matrix.append(row)
    
    for j in range(num):
        for k in range(num):
            element = input("Enter number in matrix (enter them in columns): ")
            matrix[j].append(int(element))
    
    return matrix #this returns the matrix like [[1, 2, 3] [4, 5, 6] [7, 8, 9]]

def decryptHill(cText, matrix, num):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #split into groups
    cText = cText.replace(" ", "")
    cText = cText.lower()

    cTextNumbers = []
    for m in cText:
        cTextNumbers.append(alphabet.index(m)) #changes cText into numbers
    groups = [] #would be pairs if it was only 2x2
    for i in range(int(len(cText)//num)): #integer division for full number
        group = []
        for j in range(num): #adds [num] numbers into each matrix
            group.append(cTextNumbers[(i*num)+j])
        groups.append(group)
    print(groups)

    pTextNumbers = []
    for p in groups: #for each group
        for n in range(num): #for each row in key
            a = 0
            for o in range(num): #for each item in row in key
                a += (matrix[n][o] * int(p[o]))
            a = a % 26
            pTextNumbers.append(a)
    
    pText = ""
    for number in pTextNumbers:
        print(number)
        pText = pText + alphabet[number]
    return pText

def main():
    number = int(input("How big is the matrix (n*n)? Enter n: "))
    matrix = createMatrix(number)
    ciphertext = input("Enter ciphertext: ")
    print(decryptHill(ciphertext, matrix, number))

#works for 2x2 im pretty sure but ive not tested it with 3