speedLimit = int(input("Enter the speed limit: "))
currentSpeed = int(input("Enter the recorded speed of the car: "))
if currentSpeed <= speedLimit:
    print("Congratulations, you are within the speed limit!")
else:
    if currentSpeed - speedLimit <= 20:
        print("You are speeding and your fine is $100.")
    elif currentSpeed - speedLimit >= 21 and currentSpeed - speedLimit <= 30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")
