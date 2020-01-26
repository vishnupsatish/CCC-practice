list1 = []
list2 = []
list3 = []
for i in range(int(input())):
    list1.append(input().split(" "))
for i in range(0, (len(list1))):
    for j in range(int(list1[i][0])):
        list2.append(list1[i][1])
    list2.append("\n")
string1 = ''.join(list2)
print(string1[:-1])
