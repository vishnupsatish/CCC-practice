room = []
h = int(input())
w = int(input())

for _ in range(h):
	room.append(list(map(int, input().split())))


def get_coords(num):
	coords = []
	for i in range(1, num+1):
		if i <= w and num // i <= h:
			if num % i == 0:
				coords.append((i, num // i))
	return coords


reached = []
found = "no"


def bfs(coord, done):
	if coord == (w, h):
		done = True
	all_coords = get_coords(room[coord[1] - 1][coord[0] - 1])
	if not done:
		for i in range(len(all_coords)):
			if not all_coords[i] in reached:
				reached.append(all_coords[i])
				done = bfs(all_coords[i], done)
	else:
		return done
	if done:
		return done


out = bfs((1, 1), False)
if out:
	print("yes")
else:
	print("no")