"""
Problem: CCC 2010 J5
Name: Vishnu Satish
Solution: This is a simple BFS problem.
"""

# Get the inputs
current_position = tuple(map(int, input().split()))
end_position = tuple(map(int, input().split()))


# Get all of tbe possible moves given a position
def get_possible_moves(position):
    # Get the x and y coordinates (unpacking) of the position
    x, y = position

    # Get ALL of the possible (even invalid) moves
    moves = [(x + 1, y + 2), (x + 2, y + 1), (x - 1, y - 2), (x - 2, y - 1), (x + 2, y - 1), (x + 1, y - 2),
             (x - 2, y + 1), (x - 1, y + 2)]
    filtered_moves = []

    # Now, for each move, add it to the filtered_moves list only if it is valid (not off the chessboard)
    for m in moves:
        if 9 > m[0] > 0 and 9 > m[1] > 0:
            filtered_moves.append(m)

    # Return the list with correct moves
    return filtered_moves


# BFS
def bfs(cp, ep):
    # Create a starting position in the queue with level as well
    q = [(cp, 0)]

    # While Q is not empty
    while q:

        # Get the current position along with current leve;
        now, level = q.pop(0)

        # Get all of the possible moves from the current position
        moves = get_possible_moves(now)

        # If the current position is the answer, return the current level (number of moves)
        if now == ep:
            return level

        # For each move, add the move position and the move number (level) to the queue
        for m in moves:
            q.append((m, level + 1))


# Print the level where the answer was found
print(bfs(current_position, end_position))
