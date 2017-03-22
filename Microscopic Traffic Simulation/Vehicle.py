#This module represents a vehicle and its different properties
from Environment import *
from Driver import *
import math
class Vehicle:
    vehicleTypeMap = {"bike":1,"car":2,"truck":3}
    visibilityRectangle = 10
    speedOfNearestVehicle = 0
    type = ""
    def __init__(self,id,fixed,typeOfDriver,type,direction,currentLane):
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

    def speedToNearestVehicle(self):
        return speedOfNearestVehicle

    #Take vehicles from visibility rectangle only

    def getDistancetoNearestVehicle(self):
        carDictionary = {}
        leftCoordinate = [(self.position[0] - vehicleTypeMap[self.type]/2),(self.position[1] + vehicleTypeMap[self.type]/2)]
        rightCoordinate = [(self.position[0] + vehicleTypeMap[self.type]/2),(self.position[1] + vehicleTypeMap[self.type]/2)]
        upLeftCoordinate = [leftCoordinate[0],leftCoordinate[1]+visibilityRectangle]
        upRightCoordinate = [rightCoordinate[0],rightCoordinate[1]+visibilityRectangle]
        carDictionary = env.getVehiclePositions()
        nearestVehicle = [0,0]
        distance = 400
        for key, value in carDictionary.iteritems():
            if (value.position[0] > leftCoordinate[0] and value.position[0] < rightCoordinate[0]) and (value.position[1] > rightCoordinate[1] and value.position[1] < upRightCoordinate[1]):            
                if math.hypot((value.position[0]-self.position[0]),(value.position[1]-self.position[1])) < distance:
                    distance = math.hypot((value.position[0]-self.position[0]),(value.position[1]-self.position[1]))
                    nearestVehicle[0] = value.position[0]
                    nearestVehicle[1] = value.position[1]
                    speedOfNearestVehicle = value.instantaneousVelocity
        return (nearestVehicle,distance)

   
    
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




if __name__ == "__main__":
    print "yes"
    v1=Vehicle(24244,-2,"aggressive","car","north","north")
    a=v1.selfSense()
    print(a)
