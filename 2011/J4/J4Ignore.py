# works now

done = [(0, -1),
        (0, -2),
        (0, -3),
        (1, -3),
        (2, -3),
        (3, -3),
        (3, -4),
        (3, -5),
        (4, -5),
        (5, -5),
        (5, -4),
        (5, -3),
        (6, -3),
        (7, -3),
        (7, -4),
        (7, -5),
        (7, -6),
        (7, -7),
        (6, -7),
        (5, -7),
        (4, -7),
        (3, -7),
        (2, -7),
        (1, -7),
        (0, -7),
        (-1, -7),
        (-1, -6),
        (-1, -5)]

whattodo = []
posnow = [-1, -5]

for i in range(100):
    line = input().split()


    over = False


    if line[0] == "u":
        over = False
        for i in range(1, int(line[1]) + 1):
            posnow[1] += 1
            if tuple(posnow) in done:
                over = True
            else:
                done.append(tuple(posnow))

    elif line[0] == "l":
        over = False
        for i in range(1, int(line[1]) + 1):
            posnow[0] -= 1
            if tuple(posnow) in done:
                over = True
            else:
                done.append(tuple(posnow))

    elif line[0] == "d":
        over = False
        for i in range(1, int(line[1]) + 1):
            posnow[1] -= 1
            if tuple(posnow) in done:
                over = True
            else:
                done.append(tuple(posnow))

    elif line[0] == "r":
        over = False
        for i in range(1, int(line[1]) + 1):
            posnow[0] += 1
            if tuple(posnow) in done:
                over = True
            else:
                done.append(tuple(posnow))

    elif line[0] == "q":
        break
    if (over):
        print(str(posnow[0]) + " " +  str(posnow[1]) + " " + "DANGER")
        break
    else:
        print(str(posnow[0]) + " " + str(posnow[1]) + " " + "safe")
