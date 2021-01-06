"""
Problem: CCC 2020 J5
Name: Vishnu Satish
Solution: Find all of the possible coordinates from a number then
use BFS to find whether reaching a coordinate is possible
"""

room = []
h = int(input())
w = int(input())

# Process the input
for _ in range(h):
    room.append(list(map(int, input().split())))


# Get all of the possible coordinates based on a number
def get_coords(coords):
    all_coords = []

    # Get the row and column through unpacking
    row, col = coords

    # Get the number in that coordinate
    num = room[row - 1][col - 1]

    # Iterate from 1 to the height of the room,
    # to avoid exceeding the height of the room
    for i in range(1, h + 1):

        # Iterate from 1 to the weight of the room,
        # to avoid exceeding the weight of the room
        for j in range(1, w + 1):

            # If the two numbers multiply to get the number,
            # then add it to the all_coords list
            if i * j == num:
                all_coords.append((i, j))

    # Return all of the valid coordinates
    return all_coords


# BFS function
def bfs():
    # Initialize a visited array to use O(1) lookups
    # based on the height and width of the room
    visited = []
    for _ in range(h + 1):
        visited.append([False for __ in range(w + 1)])

    # Initialize the queue
    q = [(1, 1)]

    # Main BFS loop
    while q:
        # Get the current element (FIFO)
        elem = q.pop(0)

        # if the element is the bottom-right of the room,
        # then it is possible to get there, so print yes
        if elem == (h, w):
            print('yes')
            break

        # Get all of the coords based on the current popped element
        for coord in get_coords(elem):

            # Get the row and column of the current coordinate
            row, col = coord

            # If the row and column has not been visited (again: lookups!!)
            if not visited[row][col]:
                # Add the current coordinate to the queue, then set it to visited
                q.append(coord)
                visited[row][col] = True

    # If the while loop has not been broken, then print no
    else:
        print('no')


# Call the BFS function
bfs()
