#This module represents a vehicle and its different properties
import Environment.py
import Driver.py
class Vehicle:
    def __init__(self,id,typeOfDriver,type,direction,fixed):
        self.id=id
        self.type=type
		self.fixed=fixed
        self.driver=Driver(typeOfDriver)
        self.appliedPressure=0
        self.direction=direction
        self.instantaneousAcceleration=self.driver.accelerationCoefficient*self.appliedPressure
        self.instantaneousVelocity=self.driver.accelerationCoefficient*(pow(self.appliedPressure,2))
        self.instantaneousPosition=self.driver.accelerationCoefficient*(pow(self.appliedPressure,3)) 
        if(direction=="north" or direction=="south")
            self.position=[fixed,instantaneousPosition]
        if(direction=="east" or direction=="west")
            self.position=[instantaneousPosition,fixed]
            
    def selfSense(self):
         return {"id":self.id,"type":self.type,"driver":self.Driver,"appliedPressure":self.appliedPressure,"instantaneousAcceleration":self.instantaneousAccelration,"instantaneousVelocity":self.instantaneousVelocity,"instantaneousPosition":self.instantaneousPosition}

    def getVisibilityRectangle(self):
        positionMap=Environment.getVehiclePositions()