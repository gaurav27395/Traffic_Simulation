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

