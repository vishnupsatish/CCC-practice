minutes = int(input())
listOfChores = [int(input()) for i in range(int(input()))]
possibleOrNot = []
nowMuch = 0
amount = 0
for i in range(len(listOfChores)):
    if listOfChores[i] > minutes:
        possibleOrNot.append("NO")
    else:
        possibleOrNot.append("YES")
if not("YES" in possibleOrNot):
    print(0)
else:
    for i in range(len(possibleOrNot)):
        if possibleOrNot[i] == "NO":
            del listOfChores[i]
    smallestchore = 0
    listOfChores.sort()
    for i in listOfChores:
        if nowMuch + i <= minutes:
            nowMuch += i
            amount += 1
        else:
            print(amount)
            break




        '''for i in range(0, len(listOfChores)):
            if i == 0:
                smallestchore = listOfChores[i]
            else:
                if listOfChores[i] < smallestchore:
                    smallestchore = listOfChores[i]
                    del listOfChores[i]
        if nowMuch + smallestchore <= minutes:
            nowMuch += smallestchore
            amount += 1
    print(amount)
'''