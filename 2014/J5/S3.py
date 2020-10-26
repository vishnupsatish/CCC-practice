tcs = int(input())
for _ in range(tcs):
	top = []
	branch = []
	lake = []
	for _ in range(int(input())):
		top.append(int(input()))
	top = list(reversed(top))
	no = 1
	length = len(top)
	if top[0] == 1:
		lake.append(1)
		del top[0]
		no = 2
	else:
		branch.append(top[0])
		del top[0]
	while True:
		if len(top) != 0:
			if no == top[0]:
				lake.insert(0, top[0])
				del top[0]
				no += 1
				continue
		try:
			if no == branch[0]:
				lake.insert(0, branch[0])
				del branch[0]
				no += 1
				continue
			0
		except: pass
		try:
			branch.insert(0, top[0])
			del top[0]
		except: pass
		if list(reversed(sorted(lake))) == lake and len(lake) == length:
			print("Y")
			break
		if sorted(branch) != branch and len(top) == 0:
			print("N")
			break