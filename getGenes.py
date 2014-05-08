
def getGenes(iString):
    count = 1
    newStr = ''
    j = 0
    switch = 0
    atgBreak = 1
    
    for i in iString:

        if (j == len(iString)):
            break

        if (switch == 1) and (atgBreak  == 1):
            newStr += codon

        atgBreak = 1
            
        codon = iString[j] + iString [j+1] + iString [j+2]

        if (codon == "atg"):
            switch = 1
            atgBreak = 0

        if ((codon == "tag") or (codon == "tga") or (codon == 'taa')):
            switch = 0
            print("Gene ", count, " ", newStr)
            newStr = ''
            count += 1

        j = j+3
                

print(getGenes("atgtghghghghtgaghgatghghghghghtag"))
      
