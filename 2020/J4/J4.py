longer = input()
cyc = input()
listofcyc = []
found = False
for i in range(len(cyc)):
    listofcyc.append(cyc[i:] + cyc[:i])
for elem in listofcyc:
    if elem in longer:
        print("yes")
        found = True
        break
if not found:
    print("no")