#! Author: Ryan Nacker
#! Title: Finding the GCD using the Euclidean Algorithm
#! Email: nackerr@rider.edu
#! Website: http://nackerr.me

def calcGCD(numX, numY):
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
    return (str(numList[1]) + " is the GCD of the two numers.")


while True:
    numX = input("Please enter the first number: ")
    numY = input("Please enter the second number: ")
    
    try:
        val = int(numX)
        val2 = int(numY)
        if val < 0 or val2 < 0: 
            print("Please input a positive number.")
            continue
        break
    except ValueError:
        print("The input you entered is not a number.")
print(calcGCD(int(numX), int(numY)))


