yr = int(input())
while True:
    if len(set(list(str(yr)))) == len(list(str(yr))):
        print(yr)
        break
    yr += 1