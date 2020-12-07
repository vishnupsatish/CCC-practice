"""
Problem: CCC 2014 J5
Name: Vishnu Satish
Solution: Use a simple check function to determine
whether the pair of partners are valid
"""

people = int(input())
ppl1 = input().split()
ppl2 = input().split()
pairs = dict()

# Create dictionary of all of the partnerss
for i, elem in enumerate(ppl1):
	pairs[ppl1[i]] = ppl2[i]

ok = True

# If there is an issue, and the partners
# aren't paired or a partner is paired
# with themselves, set "ok" to false
for key in pairs:
	partner1 = key
	partner2 = pairs[key]
	if pairs[partner2] != partner1:
		ok = False
		break
	if partner1 == partner2:
		ok = False
		break

# Print whether the pairs are ok or not
if ok:
	print("good")
else:
	print('bad')
