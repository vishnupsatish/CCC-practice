"""
Problem: CCC 2012 S4/J5
Name: Vishnu Satish
Solution: For each list, find all of the possible moves then perform a BFS for all of
the possible moves. Eventually, either return IMPOSSIBLE or the current level
"""


# Find all of the possible moves
def get_possible_moves(original):
    possible_moves = []
    # Iterate over the list to find all possible moves
    for i, e in enumerate(original):

        # If the current element is the middle, set neighbours to each side, but if the
        # current element is the first or the last one, set it to the one after or before
        if i == 0:
            neighbours = [i + 1]
        elif i == len(original) - 1:
            neighbours = [i - 1]
        else:
            neighbours = [i - 1, i + 1]

        # For each neighbour, add a possible move to the list to be returned
        for n in neighbours:
            possible_moves.append(original.copy())
            # If both the neighbour and current element have no coin, continue
            if possible_moves[-1][n] == '' and possible_moves[-1][i] == '':
                pass
            # If the neighbour is empty, place the coin at the top of the stack into the neighbour
            elif possible_moves[-1][n] == '':
                possible_moves[-1][n] = possible_moves[-1][i][0]
                possible_moves[-1][i] = possible_moves[-1][i].replace(possible_moves[-1][i][0], "")
            # If the current stack is empty, continue
            elif possible_moves[-1][i] == '':
                pass
            # If both the neighbour and the stack have a coin, then add the top of the
            # stack from the current to the top of the neighbour, if there is a possibility
            else:
                if possible_moves[-1][n][0] < possible_moves[-1][i][0]:
                    continue
                possible_moves[-1][n] = "".join(sorted(list(possible_moves[-1][i][0] + possible_moves[-1][n])))
                possible_moves[-1][i] = possible_moves[-1][i].replace(possible_moves[-1][i][0], "")

    unique_p = []

    # Make sure the list of moves is unique
    for move in possible_moves:
        if move not in unique_p:
            unique_p.append(move)

    # Remove the original (input) list from the return list
    return list(filter(original.__ne__, unique_p))


# Run a BFS while finding the possible moves of a given list
def determine_bfs(l):
    # Create a visited array
    visited = [l]
    # Track the level to eventually be returned
    h = [(l, 0)]
    while h:
        # Get all moves for a given list, then if it is not
        # visited, add it to the queue and mark it as visited
        to_get_moves = h.pop(0)
        all_moves = get_possible_moves(to_get_moves[0])
        for m in all_moves:
            if m == sorted(m) and '' not in m:
                return to_get_moves[1] + 1
            if m not in visited:
                h.append((m, to_get_moves[1] + 1))
                visited.append(m)

    # If there is no possible answer, return IMPOSSIBLE
    return "IMPOSSIBLE"


# Process the input, then print the value of the BFS for each test case
while True:
    n = int(input())
    if n == 0:
        break
    l = input().split()
    if sorted(l) != l:
        print(determine_bfs(l))
    else:
        print(0)
