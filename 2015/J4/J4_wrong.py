messagesList = [input().split() for i in range(int(input()))]
timePassed = 0
eachFriend = []
timeForEach = []
oneForCurrent = []
ENDTIME = []
wowTime = 0

for i in range(len(messagesList)):
    if messagesList[i][0] == "R":
        timePassed += 1
        if not(messagesList[i][1] in eachFriend):
            eachFriend.append(messagesList[i][1])
        timeForEach.append(["R", messagesList[i][1], timePassed])
    elif messagesList[i][0] == "S":
        timePassed += 1
        if not(messagesList[i][1] in eachFriend):
            eachFriend.append(messagesList[i][1])
        timeForEach.append(["S", messagesList[i][1], timePassed])
    else: 
        timePassed += (int(messagesList[i][1]) - 1)

#sprint(timeForEach)

for i in range(len(eachFriend)):
    wowTime=0
    oneForCurrent = []
    for j in timeForEach:
        if j[1] == eachFriend[i]:
            oneForCurrent.append(j)
    if len(oneForCurrent)%2!=0:
        wowTime=-1
    else:
        #print(len(oneForCurrent)/2)
        for k in range(0, int(len(oneForCurrent)), 2):
            wowTime = wowTime+oneForCurrent[k+1][2]-oneForCurrent[k][2]

    ENDTIME.append([eachFriend[i], wowTime])
for i in ENDTIME:
    for j in i:
        print(j, end=' ')
    print()
#print(ENDTIME)
