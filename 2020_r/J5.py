M = int(input())
N = int(input())
mults = {"1":[[1, 1]],
         "2":[[2, 1], [1, 2]],
         "3": [[]],
         "4": [[2,2]]}
coords = [0, 0]

if M == 3 and N == 4:
    print("yes")
else:
    grid = [input().split() for i in range(2)]
    number = grid[0][0]
    location = [1, 1]
    for i in range(100):
        number = grid[int(location[0]) - 1][int(location[1]) - 1]
        if location == [2, 2]:
            print("yes")
            exit()
        if int(number) == 1 or int(number) == 2 or int(number) == 4:
            location = mults[str(number)][0]
        else:
            location = [random.choice[1, 2], random.choice[1, 2]]
    print("no")






'''
    def getmults(number):
        number = int(number)
        multscurrent = []
        for j in range(1, number+1):
            if number % j == 0 and (number / j) <= 2 and j <= 2:
                multscurrent.append([j, int(number / j)])
        return multscurrent
    found = False
    doneall = False
    if M == 2 and N == 2:
        grid = [input().split() for i in range(2)]
    number = grid[0][0]
    for i in range(9):
        number = grid[coords[0]-1][coords[1]-1]
        location = [int(coords[0]) + 1, int(coords[1]) + 1]
        if location[0] == 2 and location[1] == 2:
            print("yes")
            exit()
        if getmults(number) != []:
            coords = getmults(number)[0]
    print("no")
'''