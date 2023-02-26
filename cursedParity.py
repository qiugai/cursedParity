import sys
while True:
    try:
        userInput = int(input("Enter an integer number to test parity: "))
        break
    except ValueError:
        print("Please input an integer only: ")
        continue
x = sys.maxsize * -1 # start from the lowest possible supported integer
lastIntStr = str(sys.maxsize)
lastInt = int(lastIntStr[len(lastIntStr)-1])
if (lastInt == 1 or lastInt == 3 or lastInt == 5 or lastInt == 7 or lastInt == 9):
    parity = False # start on odd parity
else:
    parity = True # start on even parity
while (x < sys.maxsize):
    if (x == userInput):
        if (parity == True):
            print("Integer is even.")
        else:
            print("Integer is odd.")
        exit()
    else:
        parity = not parity
        x += 1