# Horrible, horrible brute-force not-solution. DO NOT USE/RUN

l = [[], [], []]

for i in range(3):
    current = input().split()
    for inp in current:
        try:
            l[i].append(int(inp))
        except ValueError:
            l[i].append(inp)


def determine_if_one(l):
    # Rows
    changed = False
    for i, elem in enumerate(l):
        if elem.count('X') == 1:
            x_index = elem.index('X')
            changed = True
            if x_index == 0:
                l[i][0] = elem[1] - (elem[2] - elem[1])

            if x_index == 1:
                l[i][1] = elem[0] + (elem[2] - elem[0]) // 2

            if x_index == 2:
                l[i][2] = elem[1] + (elem[1] - elem[0])

    # Columns
    for i in range(3):
        if [l[0][i], l[1][i], l[2][i]].count('X') == 1:
            changed = True
            x_index = [l[0][i], l[1][i], l[2][i]].index('X')

            if x_index == 0:
                # l[0][i] = elem[1] - (elem[2] - elem[1])
                l[0][i] = l[0][i] - (l[2][i] - l[1][i])

            if x_index == 1:
                # l[i][1] = elem[0] + (elem[2] - elem[0])//2
                l[1][i] = l[0][i] + (l[2][i] - l[0][i]) // 2

            if x_index == 2:
                # l[i][2] = elem[1] + (elem[1] - elem[0])
                l[2][i] = l[1][i] + (l[1][i] - l[0][i])
    return changed


def check_array(l):
    # Check each row
    for i, row in enumerate(l):
        if 'X' in row:
            return False
        if row[2] - row[1] != row[1] - row[0]:
            return False

    # Check each column
    for i in range(3):
        if l[2][i] - l[1][i] != l[1][i] - l[0][i]:
            return False

    return True


def array_has_x(l):
    for row in l:
        if 'X' in row:
            return True

    return False


while True:
    if not determine_if_one(l):
        break

print(check_array(l))

ans = None


def recur(now):
    global ans
    print(now)
    if check_array(now):
        print('hi')
        ans = now
        return now

    if not array_has_x(now):
        return

    for x in reversed(range(-30, 31)):
        current_one = []
        for row in now:
            current_one.append(row.copy())
        for i, row in enumerate(current_one):

            if 'X' in row:
                current_one[i][row.index('X')] = x
                recur(current_one)

            current_one = []
            for row in now:
                current_one.append(row.copy())


new_l = []

for elem in l:
    new_l.append(elem.copy())



recur(new_l)

for row in ans:
    for elem in row:
        print(elem, end=' ')
    print()

