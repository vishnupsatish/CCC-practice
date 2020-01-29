antennas = int(input("How many antennas?\n"))
eyes = int(input("How many eyes?\n"))
if antennas > 2 and eyes < 5:
    print("TroyMartian")
if antennas < 7 and eyes > 1:
    print("VladSaturnian")
if antennas < 3 and eyes < 4:
    print("GraemeMercurian")
