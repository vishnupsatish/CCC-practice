spots = int(input())
parking = [input() for i in range(2)]
counter = 0
for i in range(spots):
    if parking[0][i] == "C" and parking[1][i] == "C":
        counter += 1
print(counter)