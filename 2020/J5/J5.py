# Note: THERE IS A QUICKER SOLUTION!!!!! CHECK J5_bfs.py for a quicker solution!!!

"""
Problem: CCC 2020 J5
Name: Vishnu Satish
Solution: Find all of the possible coordinates from a number then
use backtracking/DFS to find whether reaching a coordinate is possible
"""

room = []
h = int(input())
w = int(input())

# Process the input
for _ in range(h):
    room.append(list(map(int, input().split())))


# Get all of the factors of a number in tuples
def get_coords(num):
    coords = []
    for i in range(1, num + 1):
        if i <= w and num // i <= h:
            if num % i == 0:
                coords.append((i, num // i))
    return coords


reached = []
found = "no"


# Find whether going from one coordinate to another is possible
def is_possible(coord, done):
    if coord == (w, h):
        done = True

    # get all of the factors of a number (and the possible
    # next coordinates) using the aptly-named function
    all_coords = get_coords(room[coord[1] - 1][coord[0] - 1])

    # If the solution has not been found yet:
    if not done:

        # Iterate over every possible coordinate and call
        # the function recursively if it has already not been visited yet
        for i in range(len(all_coords)):
            if not all_coords[i] in reached:
                reached.append(all_coords[i])
                done = is_possible(all_coords[i], done)
    else:
        return done
    if done:
        return done


# Call the function, then print whether it is possible
out = is_possible((1, 1), False)
if out:
    print("yes")
else:
    print("no")
