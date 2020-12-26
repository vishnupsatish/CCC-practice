'''
Problem: CCC 2019 S3
Name: Vishnu Satish
Solution: Random number selection that somehow(?) gets 15/15 on
CCCGrader through random number selection, then so-called
auto-completing the rest. No idea why this works, but don't
ask questions. But I do know how it works.
'''

from random import randint

l = [[], [], []]

# Parse input
for i in range(3):
    current = input().split()
    for inp in current:
        try:
            l[i].append(int(inp))
        except ValueError:
            l[i].append(inp)


# Determine if there is a row/column that has only
# one 'X', then add it based on the surroundings
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
                l[0][i] = l[1][i] - (l[2][i] - l[1][i])

            if x_index == 1:
                # l[i][1] = elem[0] + (elem[2] - elem[0])//2
                l[1][i] = l[0][i] + (l[2][i] - l[0][i]) // 2

            if x_index == 2:
                # l[i][2] = elem[1] + (elem[1] - elem[0])
                l[2][i] = l[1][i] + (l[1][i] - l[0][i])
    return [changed, l]


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


# Continuously call the function,
# until nothing can/has been changed
while True:
    if not determine_if_one(l)[0]:
        break


# Make random choices, then "autocomplete" using
# the above function (determine_if_one), and do this
# until a valid solution is found
def random_choice():
    current_one = []
    for row in l:
        current_one.append(row[:])

    for _ in range(15):
        for i, row in enumerate(current_one):
            if 'X' in current_one[i]:
                where_x = current_one[i].index('X')
                current_one[i][where_x] = randint(-1000000, 1000000)

                maybe_ans = [[], [x[:] for x in current_one]]
                while True:
                    maybe_ans = determine_if_one(maybe_ans[1])
                    check_it = check_array(maybe_ans[1])
                    if not maybe_ans[0]:
                        current_one = maybe_ans[1]
                        break
                    if check_it:
                        return maybe_ans[1]

        current_one[i][where_x] = 'X'

    return False


# Continuously call random_choice until there is a valid answer
if not check_array(l):
    while True:
        maybe = random_choice()
        if maybe:
            l = maybe
            break

for row in l:
    for elem in row:
        print(elem, end=' ')
    print()
