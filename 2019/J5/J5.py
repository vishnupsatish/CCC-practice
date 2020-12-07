"""
Problem: CCC 2019 J5
Name: Vishnu Satish
Solution: Use regular expressions to
find all instances of a substring in a
string, then use a backtracking/DFS solution
to find the steps to get a final result
"""

import re

# Process the input
subs = []
for _ in range(3):
    subs.append(input().split())
steps, start, end = input().split()
steps = int(steps)


# Get all of the possible strings based on
# the string replacement values given as the input
def get_all_subs(_start):
    all_subs = []
    sub_indexes = []
    # Find the indexes of the substitutions to be made using regular expressions
    for elem in subs:
        sub_indexes.append([m.start() for m in re.finditer(f'(?={elem[0]})', _start)])
    # For every substitution input and every
    # substitution to be made in that input,
    # replace the old string with the string to be replaced
    for i in range(3):
        for index in sub_indexes[i]:
            new_string = _start[0:index] + subs[i][1] + _start[len(subs[i][0]) + index:]
            all_subs.append([new_string, i + 1, index + 1])
    return all_subs


done = False


# Define a recursive function to find
# the steps to get a string to the result
# string in a given number of steps
def main(string, detail_steps, current_steps=0):
    # If the value has been found in a set number of
    # steps, then don't continue the function at all
    global done
    if done:
        return

    # Get all of the possible substitutions from the given string
    all_subs = get_all_subs(string)

    # if the final string has been found in the
    # correct number of steps, print the steps then return
    if current_steps == steps and end == string:
        for elem in detail_steps:
            print(" ".join(elem))
        done = True
        return

    # If the current number of steps exceeds
    # the required number of steps, return
    elif current_steps >= steps:
        return
    _steps = detail_steps

    # For each substitution, add the step to the steps
    # list, then call the function recursively if the
    # current number of steps is less than the required number of steps
    for elem in all_subs:
        _steps = detail_steps
        if current_steps < steps:
            _steps.append([str(elem[1]), str(elem[2]), elem[0]])
            main(elem[0], _steps, current_steps=current_steps + 1)
            _steps.pop()


# Call the function
main(start, [])
