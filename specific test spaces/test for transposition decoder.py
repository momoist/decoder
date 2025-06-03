def decryptMessage(cText, e_key):
    cText = cText.replace(" ", "") #remove spaces in ciphertext
    while len(cText) % len(e_key) != 0:
        cText = cText + "X"

    pText = ""
    cTextBlock = [] #ciphertext in correct columns
    for i in range(len(e_key)): #number of columns
        #create (6) lists within cTextBlock, each list contains letters as seperate elements
        column = []
        cTextBlock.append(column)
        #should have 6 empty lists now??
    
    count = 0 #counts which letter we're on in ciphertext LMAO
    for l in range(int(len(cText)/len(e_key))): #number of rows #l would count how many rows
        for m in range(len(e_key)): #m will go from 0-6 and repeat this number of row times: keep track of which column we are in
            cTextBlock[m].append(cText[count])
            count = count + 1
    #return cTextBlock

    for j in range(len(cTextBlock[0])): #number of rows (7)
        for k in range(len(e_key)): #6
            pText = pText + cTextBlock[e_key[k]-1][int(j)] #first one is number of columns which is key size, second one is how far down the key we are
    return pText
        #return cTextBlock[e_key[k]-1][int(0)]

print(decryptMessage("DMYERA LPAMRE OSTNBI IELEEV ATHTRP CINELA RBETAM LYARAE HDYAEV IWRTET ONTYUO NCOCRE NNIGHT MISATT AERNID AAMLTI ETLEBM RARASS TEDORW EITTIH ESLTET TRAALL TBUIOH YPEOWU LILUDN SERTNA FDIIDN SMYEFL TATHME CERYFO OTWSRT GONWLI DLEWMO WENHAO USSRME HETATT SHIMTA RTEIUS ERGNYT HOUAEV RALEDA EYBEIN ONFREM BDAOTU ROUUEN EXPCET UDGETS SMISAW ERNWOH RARIEV ADLSWT KEETOO AURSOT SNIHEM ONTNHT TESEMA ISHPAP FCIISC IHESLA TITLCE AOYBUO OTHWHS FEAFRO DDETEH UJOREN NYADSI PUSETC ATHTHS IEMGTH VHAEEB AENSOT WWAAWY LHIEAI NMICIL DNETDO LEASRT GONLWY HITTAH ATMTET HRTEOC TUNESS SHAEPX SRESDE ETHEUQ LALYTS NRO", [2,3,1,4,6,5]))