#This class represents the different types of drivers in our model
#Three types of drivers have been defined:
#Aggressive
#Semi-Aggressive
#Non-Aggressive

#There are 4 parameters of every driver:
#type
#Acceleration Coefficient
#Gap Limit
#Speed Limit
import random
import math

class Driver:
    def __init__(self,type="aggressive"):
        self.accelerationCoefficient=0
        self.type=0
        self.gapLimit=0
        self.speedLimit=0

        if type=="aggressive":
            self.type=type
            self.accelerationCoefficient=6
            self.gapLimit=5
            self.speedLimit=80

        elif type=="semi aggressive":
            self.type=type
            self.accelerationCoefficient=4
            self.gapLimit=7
            self.speedLimit=60

        elif type=="non aggressive":
            self.type=type
            self.accelerationCoefficient=2
            self.gapLimit=10
            self.speedLimit=0

    def getInstantaneousPressure(self,vehicle):
        if self.type == "aggressive":
            return random.randint(8, 10)

        elif self.type == "semi aggressive":
            return random.randint(5, 7)

        elif self.type == "non aggressive":
            return random.randint(2, 4)

    def getBrakingPressure(self,vehicle,brakingDistance):
        print("Braking pressure")
        return 1000000

