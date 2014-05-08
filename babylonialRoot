from math import sqrt


def babylonianRoot(x):
    guess = 1
    for i in range (20):
        guess = (guess + ( x / guess ) ) / 2
        print(guess)

    print("The babylonian root is ", guess)


rootNum = float(input("enter the number whose root you would like to find: "))

babylonianRoot(rootNum)

print("The real root is ", sqrt(rootNum))
