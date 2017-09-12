
#! Author: Ryan Nacker
#! Title: Euclidean Algorithm to Calculate GCD
#! Email: nackerr@rider.edu


numX = int(input("Pleae enter the first number: "))
numY = int(input("Please enter the second number: "))

numQ = numX // numY
numR = numX % numY

numList = list([numX, numY, numQ, numR])

print("A: " + str(numList[0]) + "     B: " + str(numList[1]) + "     Q: " + str(numList[2]) + "     R:     " + str(numList[3]))

while(numList[3] > 0):
    numList[0] = numList[1]
    numList[1] = numList[3]
    numList[2] = numList[0] // numList[1]
    numList[3] = numList[0] % numList[1]
    print("A: " + str(numList[0]) + "     B: " + str(numList[1]) + "     Q: " + str(numList[2]) + "     R:     " + str(numList[3]))




