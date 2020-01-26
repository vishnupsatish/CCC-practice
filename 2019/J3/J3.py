inputNo = int(input())
listOfInputs = []
encodedList = []
numberOfOneSymbol = 0
for i in range(inputNo):
    listOfInputs.append(input())
for j in range(len(listOfInputs)):
    for k in range(0, len(listOfInputs[j])):
        #print(listOfInputs[j][k], listOfInputs[j][k-1])
        if k == 0:
            numberOfOneSymbol = 1
        elif listOfInputs[j][k] != listOfInputs[j][k-1]:
            encodedList.append(str(numberOfOneSymbol) + " " + listOfInputs[j][k-1] + " ")
            numberOfOneSymbol = 1
        else:
            numberOfOneSymbol += 1
        #print(numberOfOneSymbol)
        if k == len(listOfInputs[j]) - 1:
            encodedList.append(str(numberOfOneSymbol) + " " + listOfInputs[j][k-1] + " ")
    numberOfOneSymbol = 0
    encodedList.append("\n")
strAns = "".join(encodedList)
print(strAns[:-1])
        
