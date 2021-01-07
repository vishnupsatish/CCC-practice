"""
Problem: CCC 2020 J5
Name: Vishnu Satish
Solution: Find all of the possible coordinates from a number then
use DFS to find whether reaching a coordinate is possible
"""

from sys import stdin

room = []
h = int(stdin.readline())
w = int(stdin.readline())

# Process the input
for _ in range(h):
    room.append(list(map(int, stdin.readline().split())))

computed_factors = {}


# Get all of the factors of a number in the room
def get_coords(coords):
    all_coords = []

    # Get the row and column through unpacking
    row, col = coords

    # Get the number in that coordinate
    num = room[row - 1][col - 1]

    # If the factors of a number have already been computed, then return the computation
    if num in computed_factors:
        return computed_factors[num]

    # Iterate to the height, then add a pair of factors
    # only if they are valid and fit inside the room
    for x in range(1, h + 1):
        if num % x == 0 and num // x <= w:
            all_coords.append((x, num // x))

    # Set the factors of the number to be the computed factors
    computed_factors[num] = all_coords

    return all_coords


# DFS function
def dfs():
    # Initialize a visited array to use O(1) lookups
    # based on the height and width of the room
    visited = []
    for _ in range(h + 1):
        visited.append([False for __ in range(w + 1)])

    # Initialize the queue
    q = [(1, 1)]

    # Main DFS loop
    while q:
        # Get the current element (LIFO)
        elem = q[-1]
        del q[-1]

        # if the element is the bottom-right of the room,
        # then it is possible to get there, so print yes
        if elem == (h, w):
            print('yes')
            break

        # Get all of the coords based on the current popped element
        for coord in get_coords(elem):

            # Get the row and column of the current coordinate

            # If the row and column has not been visited (again: lookups!!)
            if not visited[coord[0]][coord[1]]:
                # Add the current coordinate to the queue, then set it to visited
                q.append(coord)
                visited[coord[0]][coord[1]] = True

    # If the while loop has not been broken, then print no
    else:
        print('no')


# Call the DFS function
dfs()
