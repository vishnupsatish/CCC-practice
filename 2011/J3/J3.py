sumac = [int(input()) for i in range(2)]
counter = 0
while sumac[0] >= 0 and sumac[1] >= 0:
    counter += 1
    sumac[1], sumac[0] = sumac[0] - sumac[1], sumac[1]
print(counter+1)