d = input().split()
d = [int(item) for item in d]
map = []
map.append([0,                         d[0],                 d[0] + d[1],                     d[0] + d[1] + d[2],       d[0] + d[1] + d[2] + d[3]])
map.append([d[0],                      0,                    d[1],                            d[1] + d[2],              d[1] + d[2] + d[3]])
map.append([d[0] + d[1],               d[1],                 0,                               d[2],                     d[2] + d[3]])
map.append([d[0] + d[1] + d[2],        d[1] + d[2],          d[2],                            0,                        d[3]])
map.append([d[0] + d[1] + d[2] + d[3], d[1] + d[2] + d[3],   d[2] + d[3],                     d[3],                        0])

for row in map:
    for elem in row:
        print(elem, end=" ")
    print()