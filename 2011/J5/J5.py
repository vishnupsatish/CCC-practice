"""
Problem: CCC 2011 J5
Name: Vishnu Satish
Solution: I initially thought of this problem
as a textbook DFS/BFS problem, but the more you
think about it deeply, it becomes a combinations/
checking problem. To organize it well, first create
a class Node (like a graph) where the value will be
the person, the the so-called "adjacent" nodes will
be the people that person has invited. Then, for each
number from one to N - 1, create combinations of the
range of N with the length being each number from one
to N - 1. Then, for each adjacent node of each element
of each combination, check if that adjacent node is NOT
in the original combination. If it isn't, then you have
an invalid combination, since a person to remove exists
but not the person(s) he/she has invited. Then, just print
the length of the combinations.
"""

from itertools import combinations


# Define a class Node with adjacent and value parameters
class Node:
    def __init__(self, adjacent, value):
        self.adjacent = adjacent
        self.value = value

    def __str__(self):
        return f'Node(value={self.value}, adjacent={self.adjacent})'

    def __repr__(self):
        return f'Node(value={self.value}, adjacent={self.adjacent})'


# Get the N from input
N = int(input())

# Define two lists, one where the index + 1
# holds the person that invited them, and the
# other being the list which contains all of
# the to-be nodes for each person
who_invited = []
nodes = []

# Iterate over each person, then create a Node
for i in range(1, N):
    who_invited.append(int(input()))
    node = Node(value=i, adjacent=[])
    nodes.append(node)

# Create node for Mark then add it to the nodes list
mark = Node(value=N, adjacent=[])

nodes.append(mark)

# For every node, set its adjacent
# list to all of the people it invited
for i, p in enumerate(who_invited):
    nodes[p - 1].adjacent.append(i + 1)

combs = []

# For every number from 0 to N - 1
for i in range(N):

    # Iterate over each combination with range
    # 1 to N - 1 with length as i for possible
    # combinations of people to remove
    for c in list(combinations(range(1, N), i)):

        # Set ok to True, assuming that the current combination is valid
        ok = True

        # For every person in the combinations list
        for nde in c:

            # Get the node from the graph that is associated to that person
            curr_node = nodes[nde - 1]

            # For each adjacent element of that node
            for adj in curr_node.adjacent:

                # If the adjacent element is not in the combination,
                # then it is invalid since you have removed someone
                # but not the people he/she has invited
                if adj not in c:
                    # Set ok to false then break the loop
                    ok = False
                    break

        # if the current combination is valid, add it to the list of combinations
        if ok:
            combs.append(c)

# Print the length (number) of valid
# combinations of people that can be removed
print(len(combs))
