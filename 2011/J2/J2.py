h = int(input())
maxhours = int(input())
neg = True
for t in reversed(range(1, maxhours+1)):
    tplus = t + 1
    if ((-6*(t**4)) + (h*(t**3)) + (2*(t**2)) + (t)) > 0:
        if tplus <= maxhours:
            neg = False
            print("The balloon first touches ground at hour:\n" + str(tplus))
        break
    if t == 1:
        neg = False
        print("The balloon first touches ground at hour:\n" + str(t))
        break
if neg == True:
    print("The balloon does not touch ground in the given time.")
