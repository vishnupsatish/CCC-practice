#NOT DONE YET!!!! Some edge cases do not work, please refer to IN and OUT files to debug and fix. Thanks.

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
for i in range(100):
    line = input()
    if line != "":
        whattodo.append(line.split())
    else:
        break
posnow = [-1, -5]
over = False
for inst in whattodo:
    if inst[0] == "u":
        over = False
        for i in range(1, int(inst[1]) + 1):
            posnow[1] += 1
            if tuple(posnow) in done:
                over = True
            else:
                done.append(tuple(posnow))
        #done.append(tuple(posnow))
    elif inst[0] == "l":
        over = False
        for i in range(1, int(inst[1]) + 1):
            posnow[0] -= 1
            if tuple(posnow) in done:
                over = True
            else:
                done.append(tuple(posnow))
        #done.append(tuple(posnow))
    elif inst[0] == "d":
        over = False
        for i in range(1, int(inst[1]) + 1):
            posnow[1] -= 1
            if tuple(posnow) in done:
                over = True
            else:
                done.append(tuple(posnow))
        #done.append(tuple(posnow))
    elif inst[0] == "r":
        over = False
        for i in range(1, int(inst[1]) + 1):
            posnow[0] += 1
            if tuple(posnow) in done:
                over = True
            else:
                done.append(tuple(posnow))
        #done.append(tuple(posnow))
    elif inst[0] == "q":
        break
    if (over):
        print(str(posnow[0]) + " " +  str(posnow[1]) + " " + "DANGER")
        break
    else:
        print(str(posnow[0]) + " " + str(posnow[1]) + " " + "safe")


