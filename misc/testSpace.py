cText = "33512534432111422523"
pText = ""
square = [['s', 'q', 'u', 'a', 'r'], ['e', 'f', 'g', 'h', 'i'], ['k', 'l', 'm', 'n', 'o'], ['p', 't', 'v', 'w', 'x'], ['y', 'z', 'b', 'c', 'd']]
#for i in range(int(len(cText)/2)):
 #   cTextCoords.append(cText[i*2] + cText[(i*2)+1])
#print(cTextCoords)

cTextCoords = ['33', '51', '25', '34', '43', '21', '11', '42', '25', '23']
#for j in range(len(cTextCoords)):
coords = cTextCoords[1]
row = coords[0]
column = coords[1]
print(coords)
print(row)
print(column)
pText = pText + square[int(row)-1][int(column)-1]
print(pText)