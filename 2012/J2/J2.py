fullReadings = [int(input()) for i in range(4)]
if fullReadings[0] < fullReadings[1] and fullReadings[1] < fullReadings[2] and fullReadings[2] < fullReadings[3]:
    print("Fish Rising")
elif fullReadings[3] < fullReadings[2] and fullReadings[2] < fullReadings[1] and fullReadings[1] < fullReadings[0]:
    print("Fish Diving")
elif fullReadings[3] == fullReadings[2] and fullReadings[2] == fullReadings[1] and fullReadings[1] == fullReadings[0]:
    print("Fish At Constant Depth")
else:
    print("No Fish")