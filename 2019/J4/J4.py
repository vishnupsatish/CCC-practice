list3d = [[1, 2], [3, 4]]
list2 = []
for i in input():
    if i == "H":
        list3d.append(list3d[0])
        list3d.pop(0)
    elif i == "V":
        list2 = []
        for j in range(len(list3d)):
            for k in list3d[j]:
                list2.append(k)
        list3d[0][0] = list2[1]
        list3d[0][1] = list2[0]
        list3d[1][0] = list2[3]
        list3d[1][1] = list2[2]
print(str(list3d[0][0]) + " " + str(list3d[0][1]) + "\n" + str(list3d[1][0]) + " " + str(list3d[1][1]))