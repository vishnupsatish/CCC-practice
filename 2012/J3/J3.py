original = [["*", "x", "*"], [" ", "x", "x"], ["*", " ", "*"]]
final = []
scale = int(input())
for row in original:
    for elem in row:
        final.append(elem*scale)
for i in final:
    for j in i:
        print(j, end="")
    print()
