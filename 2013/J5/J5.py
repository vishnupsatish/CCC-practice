"""
Problem: CCC 2013 J5
Name: Vishnu Satish
Solution: Use recursion to find all of the possible
results for the remaining games, and then the possible
results where the favourite team wins
"""

import itertools

t = int(input())

g = int(input())

games = {}

score_so_far = [0] * 5

# Process the input and add the games that have been
# played as well as the team that has won the game
for _ in range(g):
    t1, t2, s1, s2 = list(map(int, input().split()))
    if s1 > s2:
        games[(t1, t2)] = t1
        score_so_far[t1] += 3
    elif s1 < s2:
        games[(t1, t2)] = t2
        score_so_far[t2] += 3
    else:
        games[(t1, t2)] = 't'
        score_so_far[t1] += 1
        score_so_far[t2] += 1

# Get all of the possible games that need to be played
need_to_play = list(itertools.combinations([1, 2, 3, 4], 2))

# Remove all of the games that have been played
need_to_play = list(set(need_to_play) ^ set(games))

ans = 0


# Recursive function to get all of the possible wins
def get_possible_wins(results, score, need):
    global ans

    # If all of the games have been played, then increment the possible
    # wins for the favourite team if they have won, regardless return
    if len(need) == 0:
        if score[t] == max(score) and score.count(max(score)) == 1:
            ans += 1
        return

    # For each possibility (team 1, team 2, tie)
    for poss in [need[0][0], need[0][1], 't']:
        new_results = results.copy()
        new_results[need[0]] = poss
        new_score = score.copy()

        # Add item to the list, depending on which team has won
        if poss == 't':
            new_score[need[0][0]] += 1
            new_score[need[0][1]] += 1
        else:
            new_score[poss] += 3

        # Call the function again
        get_possible_wins(new_results, new_score, need[1:])


# Call the recursive function with the current values (based on what has been played and the results)
get_possible_wins(games, score_so_far, need_to_play)

print(ans)
