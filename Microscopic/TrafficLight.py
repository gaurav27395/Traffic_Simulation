from threading import Timer

class TrafficLight:
    def __init__(self):
        self.allowedDirection = 0
        self.trafficTimeout = 5
        self.directionArray = ["northRight", "eastDown", "southLeft", "westUp"]
        self.directionIndex = 0


    def changeTrafficDirection(self):
        self.directionIndex = (self.directionIndex + 1) % 4
        self.allowedDirection = self.directionArray[self.directionIndex]
        Timer(8, self.changeTrafficDirection).start()
        file=open('signal.txt','w')
        file.write(self.allowedDirection)
        file.close()


TrafficLight().changeTrafficDirection()

