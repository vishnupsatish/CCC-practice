lines = int(input())
table = [input().split() for i in range(lines)]
rot90 = [[0 for j in range(lines)] for i in range(lines)]
rot180 = [[0 for j in range(lines)] for i in range(lines)]
rot270 = [[0 for j in range(lines)] for i in range(lines)]
testList = []
testTwo = []
correctNow = True
correct270 = True
correct180 = True
correct90 = True
whichOne = ""
#for rotating 360
#check if correct
for i in range(1, len(table)):
    if int(table[i][0]) < int(table[i - 1][0]):
        correctNow = False
for i in range(0, len(table)):
    for j in range(1, len(table[i])):
        if int(table[i][j]) < int(table[i][j -1]):
            correctNow = False
if correctNow == True:
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if j == lines - 1:
                print(table[i][j], end="")
            else:
                print(table[i][j], end=" ")
        print()
    #exit()

#for rotating 270
for i in reversed(range(len(table))):
    for j in range(len(table)):
        rot270[len(table) - 1 - j][i] = int(table[i][j])

#check if correct
for i in range(1, len(rot270)):
    if rot270[i][0] < rot270[i - 1][0]:
        correct270 = False
for i in range(0, len(rot270)):
    for j in range(1, len(rot270[i])):
        if rot270[i][j] < rot270[i][j -1]:
            correct270 = False
if correct270 == True:
    for i in range(0, len(rot270)):
        for j in range(0, len(rot270[i])):
            if j == lines - 1:
                print(rot270[i][j], end="")
            else:
                print(rot270[i][j], end=" ")
        print()
    #exit()

#for rotating 180
for i in reversed(range(len(table))):
    for j in reversed(range(len(table))):
        rot180[len(table) - 1 - i][len(table) - 1 - j] = int(table[i][j])

#check if correct
for i in range(1, len(rot180)):
    if rot180[i][0] < rot180[i - 1][0]:
        correct180 = False
for i in range(0, len(rot180)):
    for j in range(1, len(rot180[i])):
        if rot180[i][j] < rot180[i][j - 1]:
            correct180 = False
if correct180 == True:
    for i in range(0, len(rot180)):
        for j in range(0, len(rot180[i])):
            if j == lines - 1:
                print(rot180[i][j], end="")
            else:
                print(rot180[i][j], end=" ")
        print()
    #exit()


#for rotating 90
for i in reversed(range(len(rot270))):
    for j in reversed(range(len(rot270))):
        rot90[len(rot270) - 1 - i][len(rot270) - 1 - j] = int(rot270[i][j])

# check if correct
for i in range(1, len(rot90)):
    if rot90[i][0] < rot90[i - 1][0]:
        correct90 = False
for i in range(0, len(rot90)):
    for j in range(1, len(rot90[i])):
        if rot90[i][j] < rot90[i][j - 1]:
            correct90 = False
if correct90 == True:
    for i in range(0, len(rot90)):
        for j in range(0, len(rot90[i])):
            if j == lines - 1:
                print(rot90[i][j], end="")
            else:
                print(rot90[i][j], end=" ")
        print()
    #exit()


'''

for i in range(0, len(rot90)):
    for j in range(0, len(rot90[i])):
        if j == lines - 1:
            print(rot180[i][j], end="")
        else:
            print(rot180[i][j], end=" ")
    print()

for i in range(0, len(rot180)):
    for j in range(0, len(rot90[i])):
        if j == lines - 1:
            print(rot180[i][j], end="")
        else:
            print(rot180[i][j], end=" ")
    print()

for i in range(0, len(rot270)):
    for j in range(0, len(rot90[i])):
        if j == lines - 1:
            print(rot180[i][j], end="")
        else:
            print(rot180[i][j], end=" ")
    print()
    
'''