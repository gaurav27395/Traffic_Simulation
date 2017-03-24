from threading import Timer

allowedDirection = "north"
trafficTimeout = 6
directionArray = ["north", "east", "south", "west"]
directionIndex = 0


def changeDirection():
    globals()["directionIndex"] = (directionIndex + 1) % 4
    globals()["allowedDirection"] = directionArray[directionIndex]
    Timer(trafficTimeout, changeDirection).start()
    print(directionArray[directionIndex])


Timer(trafficTimeout, changeDirection).start()
