
import string

def isPalindrome(iString):
        revString = ""
        for i in iString:
                revString = i + revString
        if (iString != revString):
                return 'n'
        else:
                return 'y'

yesOrNo = 1

while (yesOrNo == 1):

    toTest = input("Enter a phrase to test for palindromitizationality: ")

    if ((isPalindrome(toTest)) == 'n'):
            print(toTest, " is not a palindrome.")
    else:
            print(toTest, "is a palindrome.")
        
    temp = input("Would you like to continue? ")

    temp = temp.lower()

    if (temp[0] == 'y'):
            yesOrNo = 1
    else:
            yesOrNo = 0
        





