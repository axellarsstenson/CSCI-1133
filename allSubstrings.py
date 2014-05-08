

def subs(iString):
    subList = []
    
    for i in range(1, len(iString)):                #iterates through the possible length of the substring 'i'
        for j in range(len(iString)):               #iterates through the possible starting locations of the substring 'j'
            tempStr = iString[j: j+i]               #sets a temporary string to a substring of length i, starting at location j
            if (tempStr not in subList):            #checks to see if it is in subList
                subList += [tempStr]                #adds tempStr to subList if tempStr is not in subList

    return subList

print(subs("tooeppe"))

