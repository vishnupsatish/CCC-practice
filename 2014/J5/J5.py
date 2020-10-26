people = int(input())
ppl1 = input().split()
ppl2 = input().split()
pairs = dict()


for i, elem in enumerate(ppl1):
	pairs[ppl1[i]] = ppl2[i]

ok = True

for key in pairs:
	partner1 = key
	partner2 = pairs[key]
	if pairs[partner2] != partner1:
		ok = False
		break
	if partner1 == partner2:
		ok = False
		break


if ok:
	print("good")
else:
	print('bad')


