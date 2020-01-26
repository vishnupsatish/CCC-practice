hour, min = input().split(":")
hour = int(hour)
min = int(min)
time = hour + min
rushhour = [(7, 8, 9), (15, 16, 17, 18)]
trv = 2
km = 120
for i in range(100):
    if hour in rushhour[1] or hour in rushhour [0]:
        km -= 5
    else:
        km -= 10
    if min != 50:
        min += 10
    elif min == 50 and hour < 23:
        hour += 1
        min = 0
    else:
        hour = 0
        min = 0
    if km == 0:
        break
if len(str(hour)) == 1:
    hour = "0" + str(hour)
if str(min) == "0":
    min = str(min) + "0"
print(str(hour) + ":" + str(min))
