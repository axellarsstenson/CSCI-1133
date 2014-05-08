import math
import random

class vec3:

    def __init__(self, vectorList = [0,0,0]):

        self.vL = vectorList

    def __str__(self):

        return "[" + str(self.vL[0]) + ", " + str(self.vL[1]) + ", " + str(self.vL[2]) + "]"

    def vlist(self):

        return self.vL

    def setValues(self, other):

        self.vL = other

    def __float__(self):

        mag = 0
        for i in range(len(self.vL)):
            mag = mag + math.pow(self.vL[i], 2)

        return math.sqrt(mag)

    def __add__(self, other):

        addList = [0, 0, 0]
        for i in range(len(self.vL)):
            addList[i] = self.vL[i] + other.vL[i]            

        return vec3(addList)

    def __mul__(self, scalar):

        mulVec = vec3()
        for i in range(len(self.vL)):
            mulVec.vL[i] = self.vL[i] * scalar

        return mulVec.vL


class particle:

    def __init__(self, mass = float(1), pos = vec3(), vel = vec3()):

        self.m = mass
        self.p = pos
        self.v = vel

    def __str__(self):

        return "\t{mass=" + str(self.m) + ",position=" + str(self.p) + ",velocity=" + str(self.v) + "}"

    def setMass(self, newMass):

        self.vL[0] = newMass
        
        return self.vL

    def momentum(self):

        return (self.v * self.m)

    def accelerate(self, a, t):

        newVel = [0, 0, 0]
        newPos = [0, 0, 0]
        tempV = self.v.vlist()
        tempP = self.p.vlist()
        
        for i in range(len(self.v.vlist())):
            newVel[i] = tempV[i] + (a[i]*t)    

        for i in range(len(self.p.vlist())):
            newPos[i] = tempP[i] + (tempP[i] * t) + (0.5 * ((a[i]*t)**2))

        return particle(self.m, vec3(newVel), vec3(newPos))

particleList = []
random.seed()

for i in range(20):
    x = random.randint(0,100)
    y = random.randint(0,100)
    newPos =vec3([x, y, 0])
    newPar = particle(1,newPos,)
    
    particleList.append(newPar)

for i in range(20):
    particleList[i].accelerate([0,0,9.8], 10)
    
for i in particleList:
    print(i)
    




v1 = vec3([2,3,4])
v2 = vec3([1,1,1])
print(v1)
print(float(v1))
print(v1 + v2)
p1 = particle(5, v2, v1)
print(p1)
print(p1.momentum())


    
