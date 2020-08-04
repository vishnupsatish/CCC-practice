coords = [input().split(",") for i in range(int(input()))]
leastx = 100
leasty = 100
mostx = 0
mosty = 0
for eachcor in coords:
    if int(eachcor[0]) < int(leastx):
        leastx = int(eachcor[0])
    if int(eachcor[0]) > int(mostx):
        mostx = int(eachcor[0])
    if int(eachcor[1]) < int(leasty):
        leasty = int(eachcor[1])
    if int(eachcor[1]) > int(mosty):
        mosty = int(eachcor[1])
mosty += 1
mostx += 1
leasty -= 1
leastx -= 1
print(str(leastx) + "," + str(leasty) + "\n" + str(mostx) + "," + str(mosty))