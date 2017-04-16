from threading import Timer
from Microscopic.Environment import *
from Microscopic.smartTraffic import *
import operator

class TrafficLight:
    strategyToUse = "Normal"
    def __init__(self):
        self.allowedDirection = 0
        self.trafficTimeout = 5
        self.directionArray = ["northRight", "eastDown", "southLeft", "westUp"]
        self.directionIndex = 0


    def changeTrafficDirection(self):
        self.directionIndex = (self.directionIndex + 1) % 4
        self.allowedDirection = self.directionArray[self.directionIndex]
        file = open('signal.txt', 'w')
        file.write(self.allowedDirection)
        file.close()


        if self.strategyToUse=="Count":
            seconds=countOfVehicles[self.directionArray[self.directionIndex]]

            if seconds==0 or seconds==1:
                seconds=2

            Timer(seconds,self.changeTrafficDirection).start()

        elif self.strategyToUse=="Time":
            timingList=Timing
            dc_sort = sorted(timingList.items(), key=operator.itemgetter(1), reverse=True)
            seconds=int(dc_sort[self.directionIndex][1])/100

            if seconds == 0 or seconds == 1:
                seconds = 2
            Timer(seconds, self.changeTrafficDirection).start()

        elif self.strategyToUse=="Normal":
            Timer(8, self.changeTrafficDirection).start()




TrafficLight().changeTrafficDirection()

