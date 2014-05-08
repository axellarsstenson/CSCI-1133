

def bsearch(searchTerm, searchList, low = 0, high = None):

    if high == None and low == 0:
        low = 0
        high = len(searchList) - 1

    while high >= low:
    
        position = (high + low) // 2

        if searchTerm > searchList[position]:
            low = position + 1
            bsearch(searchTerm, searchList, low, high)

        elif searchTerm < searchList[position]:
            high = position - 1
            bsearch(searchTerm, searchList, low, high)

        else:
            return position

    return None


def main():

    searchList = []
    for term in range(11):
        searchList.append(term)

    i = 11
    while i >= 0:
        print(bsearch(i, searchList))
        i -= 1
        
main()
    
