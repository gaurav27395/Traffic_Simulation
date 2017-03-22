#This module represents a vehicle and its different properties
from Environment import *
from Driver import *

class Vehicle:
    def __init__(self,id,fixed,typeOfDriver,type,direction):
        self.id=id
        self.type=type
        self.fixed=fixed
        self.driver=Driver(typeOfDriver)
        self.appliedPressure=2
        self.direction=direction
        self.instantaneousAcceleration=self.driver.accelerationCoefficient*self.appliedPressure
        self.instantaneousVelocity=self.driver.accelerationCoefficient*(pow(self.appliedPressure,2))
        self.instantaneousPosition=self.driver.accelerationCoefficient*(pow(self.appliedPressure,3)) 
        if(direction=="north" or direction=="south"):
            self.position=[fixed,self.instantaneousPosition]
        if(direction=="east" or direction=="west"):
            self.position=[self.instantaneousPosition,fixed]
                                                                                                      
    def selfSense(self):
         return {"id":self.id,"type":self.type,"driver":self.driver.type,"appliedPressure":self.appliedPressure,"instantaneousAcceleration":self.instantaneousAcceleration,"instantaneousVelocity":self.instantaneousVelocity,"instantaneousPosition":self.instantaneousPosition}

    def getVisibilityRectangle(self):
        positionMap=getVehiclePositions()

    def print(self):
        print(self.id)
        print(self.type)
        print(self.driver.type)
        print(self.driver.gapLimit)
        print(self.direction)
        print(self.instantaneousAcceleration)
        print(self.instantaneousVelocity)
        print(self.instantaneousPosition)
        print(self.position)
    
    def getLaneSignalPosition(self):
        lanePosition = self.currentLane.trafficPosition()
        selfPosition = self.instantaneousPosition
        return hypot((lanePosition[0]-selfPosition[0]),(lanePosition[1]-selfPosition[1]))

    def vehicleAcceleration(self):
        if self.direction == 'north' or self.direction == 'south':
            a = self.instantaneousVelocity*0.05 + self.instantaneousAcceleration*0.5*0.05*0.05 # ut+0.5at^2
            self.position[1]=self.position[1]+a
            self.instantaneousVelocity = self.instantaneousAcceleration*0.05
        if self.direction == 'east' or self.direction == 'west':
            a = self.instantaneousVelocity*0.05 + self.instantaneousAcceleration*0.5*0.05*0.05 # ut+0.5at^2
            self.position[0]=self.position[0]+a
            self.instantaneousVelocity = self.instantaneousAcceleration*0.05

    def vehicleBrake(self):
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




v1=Vehicle(24244,-2,"aggressive","car","north")
a=v1.print()
a=v1.selfSense()
print(a)
