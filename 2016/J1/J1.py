wins = 0
for i in range(6):
    if input() == "W":
        wins += 1
if wins > 4:
    print(1)
elif wins == 3 or wins == 4:
    print(2)
elif wins == 2 or wins == 1:
    print(3)
else:
    print(-1)
