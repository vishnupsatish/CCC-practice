import itertools

t = int(input())

g = int(input())

games = {}

score_so_far = [0] * 5

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

need_to_play = list(itertools.combinations([1, 2, 3, 4], 2))

need_to_play = list(set(need_to_play) ^ set(games))

ans = 0


def get_possible_wins(results, score, need):
	global ans
	if len(need) == 0:
		if score[t] == max(score) and score.count(max(score)) == 1:
			ans += 1
		return

	for poss in [need[0][0], need[0][1], 't']:
		new_results = results.copy()
		new_results[need[0]] = poss
		new_score = score.copy()
		if poss == 't':
			new_score[need[0][0]] += 1
			new_score[need[0][1]] += 1
		else:
			new_score[poss] += 3
		get_possible_wins(new_results, new_score, need[1:])


get_possible_wins(games, score_so_far, need_to_play)

print(ans)


