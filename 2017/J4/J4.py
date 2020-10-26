time = "12:00"
minutes = int(input())

times = minutes // 720
minutes = minutes % 720

def get_all_times(time):
	global minutes
	ans = 31 * times
	if minutes >= 60:
		now_minutes = 59
	else:
		now_minutes = minutes
	for hour in range(minutes // 60 + 1):
		for minute in range(0, now_minutes):
			new_min = str(int(time[-2:]) + 1)
			if len(new_min) < 2:
				new_min = "0" + new_min
			time = time[:-2] + new_min
			#print(time)
			seq = check_sequence(time)
			ans += seq
			#if seq == 1:
				#print("this is sequence, now ans is ", ans)

		minutes -= 60
		if minutes >= 60:
			now_minutes = 59
		else:
			now_minutes = minutes
		if minutes > 0:
			if time[0:2] == "12":
				time = "1:00"
			else:
				time = str(int(time[0:time.index(':')]) + 1) + ":" + "00"
			#print(time)
			seq = check_sequence(time)
			ans += seq
			#if seq == 1:
				#print("this is sequence, now ans is ", ans)
	return ans




def check_sequence(time):
	new_time = time[0:time.index(":")] + time[time.index(":") + 1:]
	common = int(new_time[1]) - int(new_time[0])
	for i, digit in enumerate(new_time[1:], start=1):
		digit = int(digit)
		if digit - int(new_time[i - 1]) != common:
			return 0
	return 1


ans = get_all_times(time)

print(ans)
