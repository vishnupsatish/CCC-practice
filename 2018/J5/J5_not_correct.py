def minus1(num):
	return num - 1

pages = int(input())
temp_pages_reachable = [list(map(minus1, list(map(int, input().split())))) for _ in range(pages)]
pages_reachable = []
end_pages = []
visited = dict()



for page in range(len(temp_pages_reachable)):
	if temp_pages_reachable[page][0] == -1:
		end_pages.append(page)
	pages_reachable.append(list(set(temp_pages_reachable[page])))
	visited[page] = []
del temp_pages_reachable
visited[-1] = []

shortest_step = 10000000000000000000


def main(page_no, steps=0):
	global shortest_step
	if page_no == -1 and steps < shortest_step:
		shortest_step = steps
	for reachable in pages_reachable[page_no]:
		if reachable in visited[page_no]:
			continue
		visited[page_no].append(reachable)
		main(reachable, steps=steps+1)
		steps -= 1


main(0)

for key in visited:
	if len(visited[key]) == 0:
		print("N")
		break
else:
	print("Y")

print(shortest_step)





#-------------------------------------------------------------------------------------------------
# Wrong answer below



# def bfs():
# 	visited_ = dict()
# 	q = [0]
# 	visited_[0] = True
# 	for page in range(pages):
# 		visited_[page] = False
# 	visited_[-1] = False
# 	level = 0
# 	ans = 238929843743738
# 	while q:
#
# 		now = pages_reachable[q.pop(0)]
#
# 		for v in now:
# 			if not visited_[v]:
# 				visited_[v] = True
# 				q.append(v)
# 				# print(v + 1, level, end="\n")
# 				if v == -1:
# 					return len(q)
# 				level -= 1
# 		level += 1


# def bfs(nodes, level):
# 	level += 1
# 	for node in nodes:
# 		node_ = pages_reachable[node]
# 		if -1 in node_:
# 			return level
# 	return bfs(node_, level)