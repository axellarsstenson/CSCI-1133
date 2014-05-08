import random

countList = [ 0, 0, 0, 0, 0, 0 ]
random.seed()
for i in range(1000):
    tempRand = random.randint(1, 6)
    if (tempRand== 1):
        countList[0] += 1
    elif (tempRand == 2):
        countList[1] += 1
    elif (tempRand == 3):
        countList[2] += 1
    elif (tempRand == 4):
        countList[3] += 1
    elif (tempRand == 5):
        countList[4] += 1
    elif (tempRand == 6):
        countList[5] += 1

print(countList)
