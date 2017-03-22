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

    def pressAcceleration(self):
        if self.direction == 'north' or self.direction == 'south':
            a = self.instantaneousVelocity*0.05 + self.instantaneousAcceleration*0.5*0.05*0.05 # ut+0.5at^2
            self.position[1]=self.position[1]+a
            self.instantaneousVelocity = self.instantaneousAcceleration*0.05
        if self.direction == 'east' or self.direction == 'west':
            a = self.instantaneousVelocity*0.05 + self.instantaneousAcceleration*0.5*0.05*0.05 # ut+0.5at^2
            self.position[0]=self.position[0]+a
            self.instantaneousVelocity = self.instantaneousAcceleration*0.05

    def pressBrake(self):
        if self.direction == 'north' or self.direction == 'south':
            a = self.instantaneousVelocity*0.05 + self.instantaneousAcceleration*0.5*0.05*0.05 # ut+0.5at^2
            if a > 0 :
                self.position[1]=self.position[1]+a
                self.instantaneousVelocity = self.instantaneousAcceleration*0.05
        if self.direction == 'east' or self.direction == 'west':
            a = self.instantaneousVelocity*0.05 + self.instantaneousAcceleration*0.5*0.05*0.05 # ut+0.5at^2
            if a > 0 :
                self.position[0]=self.position[0]+a
                self.instantaneousVelocity = self.instantaneousAcceleration*0.05


