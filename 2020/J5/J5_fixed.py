M = int(input())
N = int(input())
grid = [input().split() for i in range(M)]
wentthrough = []
needthrough = []
done = False
found = False
d = dict()


def factor(number):
    number = int(number)
    factored = []
    for i in range(1, int(number) + 1):
        if number % i == 0 and i <= M and number / i <= N:
            factored.append([i, int(number / i)])
    return factored


def check(coords):
    x = coords[0]
    y = coords[1]
    global found
    d[str(coords[0]) + "," + str(coords[1])] = True
    # print(str(coords) + "\n" + str(grid[x][y]) + "\n\n")
    every = factor(grid[x - 1][y - 1])
    if not found:
        for elem in every:
            if elem == [M, N]:
                found = True
            else:
                if d.get(str(elem[0]) + "," + str(elem[1]), -1) == -1:
                    d[str(elem[0]) + "," + str(elem[1])] = False
                if d[str(elem[0]) + "," + str(elem[1])] == False:
                    check(elem)
    return found


if check([1, 1]):
    print('yes')
else:
    print("no")
