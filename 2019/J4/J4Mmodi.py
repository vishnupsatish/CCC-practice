list3d = [1, 2, 3, 4]

for i in input():
    if i == "H":
        list3d[2], list3d[0] = list3d[0], list3d[2]
        list3d[1], list3d[3] = list3d[3], list3d[1]
    else:
        list3d[0], list3d[1] = list3d[1], list3d[0]
        list3d[2], list3d[3] = list3d[3], list3d[2]
print(str(list3d[0]) + " " + str(list3d[1]) + "\n" + str(list3d[2]) + " " + str(list3d[3]))


'''
for i in input():
    if i == "H":
        list3d.append(list3d[0])
        list3d.append(list3d[1])
        list3d.pop(0)
        list3d.pop(1)
    elif i == "V":
        list3d.append(list3d[1])
        list3d.append(list3d[0])
        list3d.append(list3d[3])
        list3d.append(list3d[2])
        list3d
for i in list3d:
    for j in i:
        print(j, end=' ')
    print()
'''
