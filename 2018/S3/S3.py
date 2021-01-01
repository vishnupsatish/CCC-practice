row, column = list(map(int, input().split()))

arr = []

for _ in range(row):
    arr.append(list(input()))

conveyors = ['U', 'D', 'L', 'R']


def camera_positions():
    pos = []
    camera_position = []
    for i, row_ in enumerate(arr):
        for j, elem in enumerate(row_):
            if elem == 'C':
                camera_position.append((i, j))

    for c in camera_position:
        for j in range(1, row + 1):
            i = c[0]
            current = arr[i][c[1] + j]
            try:
                if current == 'W':
                    break
                if current in conveyors:
                    continue
            except IndexError:
                break
            pos.append((i, c[1] + j))

        for j in range(1, row + 1):
            i = c[0]
            current = arr[i][c[1] - j]
            # print((i, c[1] - j), current)
            if c[1] - j < 0:
                break
            if current == 'W':
                break
            if current in conveyors:
                continue
            pos.append((i, c[1] - j))

        for i in range(1, row + 1):
            j = c[1]
            current = arr[c[0] + i][j]
            # print((c[0] + i, j), current)
            try:
                if current == 'W':
                    break
                if current in conveyors:
                    continue
            except IndexError:
                break

            pos.append((c[0] + i, j))

        for i in range(1, row + 1):
            j = c[1]
            current = arr[c[0] - i][j]
            # print((c[0] - i, j), current)
            if c[0] - i < 0:
                break
            if current == 'W':
                break
            if current in conveyors:
                continue

            pos.append((c[0] - i, j))

    return pos


cam_pos = camera_positions()


# for pos in cam_pos:
#     print(pos, arr[pos[0]][pos[1]])


def get_s_position():
    for i, row in enumerate(arr):
        for j, elem in enumerate(row):
            if elem == 'S':
                return (i, j)


def get_movable_positions(pos=get_s_position()):
    i, j = pos
    correct = []
    possible = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
    for to_i, to_j in possible:
        if arr[to_i][to_j] != 'W' and (to_i, to_j) not in cam_pos:
            correct.append((to_i, to_j))
    return correct


def move_down(pos):
    i, j = pos
    new = arr[i][j]
    visited.append((i, j))
    if new == 'W' or new == 'U':
        return False
    if new == '.':
        return (i, j)
    if new == 'L':
        return move_left((i + 1, j))
    if new == 'R':
        return move_right((i + 1, j))
    if new == 'D':
        return move_down((i + 1, j))


def move_up(pos):
    i, j = pos
    new = arr[i][j]
    visited.append((i, j))
    if new == 'W' or new == 'D':
        return False
    if new == '.':
        return (i, j)
    if new == 'L':
        return move_left((i - 1, j))
    if new == 'R':
        return move_right((i - 1, j))
    if new == 'U':
        return move_up((i - 1, j))


def move_right(pos):
    i, j = pos
    new = arr[i][j]
    visited.append((i, j))
    if new == 'W' or new == 'L':
        return False
    if new == '.':
        return (i, j)
    if new == 'D':
        return move_down((i, j + 1))
    if new == 'U':
        return move_up((i, j + 1))
    if new == 'R':
        return move_right((i, j + 1))


visited = [(get_s_position())]


def move_left(pos):
    i, j = pos
    new = arr[i][j]
    visited.append((i, j))
    if new == 'W' or new == 'R':
        return False
    if new == '.':
        return (i, j)
    if new == 'D':
        return move_down((i, j - 1))
    if new == 'U':
        return move_up((i, j - 1))
    if new == 'L':
        return move_left((i, j - 1))


def bfs():
    ans = []
    q = [(get_s_position(), 0)]
    while q:
        now = q.pop(0)

        for pos in get_movable_positions(now[0]):
            if pos in visited:
                continue
            i, j = pos
            if arr[i][j] in conveyors:

                if arr[i][j] == 'L':
                    new = move_left((i, j))

                elif arr[i][j] == 'R':
                    new = move_right((i, j))

                elif arr[i][j] == 'U':
                    new = move_up((i, j))

                elif arr[i][j] == 'D':
                    new = move_down((i, j))

                if new:
                    q.append((new, now[1] + 1))
                    visited.append(new)
                    i, j = new
                    if arr[i][j] == '.':
                        ans.append((new, now[1] + 1))

                continue
            q.append((pos, now[1] + 1))
            if arr[i][j] == '.':
                ans.append((pos, now[1] + 1))
            visited.append(pos)
    return ans


ans = bfs()

coords_ans = list(map(lambda x: x[0], ans))

beside_c = False
for pos in get_movable_positions():
    i, j = pos
    if arr[i][j] == 'C':
        for i, row in enumerate(arr):
            for j, elem in enumerate(row):
                if elem == '.':
                    print(-1)
                    beside_c = True

if not beside_c:
    for i, row in enumerate(arr):
        for j, elem in enumerate(row):
            if elem == '.':
                if (i, j) in coords_ans:
                    print(ans[coords_ans.index((i, j))][1])
                else:
                    print(-1)
