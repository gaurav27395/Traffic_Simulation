# This module represents a vehicle and its different properties
from Microscopic.Environment import *
from Microscopic.Driver import *
from Microscopic.Behaviour import *
from Microscopic.TrafficLight import *
import math

timeUnit = 0.1


class Vehicle:

    def __init__(self, id, fixed, typeOfDriver, type, direction):
        self.id = id
        self.type = type
        self.fixed = fixed
        self.driver = Driver(typeOfDriver)
        self.appliedPressure = 2
        self.direction = direction
        self.instantaneousAcceleration = 0
        self.instantaneousVelocity = random.randint(5, 10)
        self.instantaneousPosition = 0
        self.position = 0
        self.vehicleTypeMap = {"bike": 1, "car": 2, "bus": 3}
        self.hasToStop=False
        self.guiRectangle=None
        self.guiTimer=None
        self.timer=None
        self.doNotStop=False
        self.entryTime=0
        self.exitTime=0
        self.waitingTimeAdded=False
        self.isMoving=True

        if direction == "northRight":
            self.instantaneousPosition = random.randint(0, 50)

        elif direction == "eastDown":
            self.instantaneousPosition = random.randint(1250, 1300)

        elif direction == "southLeft":
            self.instantaneousPosition = random.randint(650, 720)

        elif direction == "westUp":
            self.instantaneousPosition = random.randint(0, 50)


        if direction == "northRight" or direction == "southLeft":
            self.position = [fixed, self.instantaneousPosition]

        if direction == "eastDown" or direction == "westUp":
            self.position = [self.instantaneousPosition, fixed]

        self.visibilityRectangle = 10


    def selfSense(self):
        return {"id": self.id, "type": self.type, "driver": self.driver.type, "appliedPressure": self.appliedPressure,
                "instantaneousAcceleration": self.instantaneousAcceleration,
                "instantaneousVelocity": self.instantaneousVelocity,
                "instantaneousPosition": self.instantaneousPosition}

    def getVisibilityRectangle(self):
        positionMap = getEnvironmentInformation()

    def speedOfNearestVehicle(self):
        return self.getInformationOfNearestVehicle()[2]

    # Take vehicles from the vehicle's visibility rectangle only

    def getInformationOfNearestVehicle(self):
        currentCoordinate=getCanvasReference().coords(self.guiRectangle)

        if countOfVehicles[self.direction]>=1:
            for id in vehicleStatusMap:
                otherVehicle=vehicleStatusMap[id]
                currentCoordinateOfOtherVehicle=getCanvasReference().coords(otherVehicle.guiRectangle)

                if otherVehicle.direction== self.direction:
                   if self.direction=="northRight" and otherVehicle.position[1]>self.position[1]:
                        if currentCoordinateOfOtherVehicle[0]>currentCoordinate[0] and currentCoordinateOfOtherVehicle[0]<currentCoordinate[2]:
                            return [otherVehicle,abs(self.position[1]-otherVehicle.position[1])]

                        elif currentCoordinateOfOtherVehicle[2]>currentCoordinate[2] and currentCoordinateOfOtherVehicle[2]<currentCoordinate[2]:
                            return [otherVehicle,abs(self.position[1]-otherVehicle.position[1])]

                        elif currentCoordinate[2]>currentCoordinateOfOtherVehicle[0] and currentCoordinate[0]<currentCoordinateOfOtherVehicle[2]:
                            return [otherVehicle,abs(self.position[1]-otherVehicle.position[1])]

                        elif currentCoordinate[0]>currentCoordinateOfOtherVehicle[0] and currentCoordinate[2]<currentCoordinateOfOtherVehicle[0]:
                            return [otherVehicle,abs(self.position[1]-otherVehicle.position[1])]

                   elif self.direction=="southLeft" and otherVehicle.position[1]<self.position[1]:
                       if currentCoordinateOfOtherVehicle[0] > currentCoordinate[0] and currentCoordinateOfOtherVehicle[
                           0] < currentCoordinate[2]:
                           return [otherVehicle,abs(self.position[1]-otherVehicle.position[1])]

                       elif currentCoordinateOfOtherVehicle[2] > currentCoordinate[2] and \
                                       currentCoordinateOfOtherVehicle[2] < currentCoordinate[2]:
                           return [otherVehicle,abs(self.position[1]-otherVehicle.position[1])]

                       elif currentCoordinate[2] > currentCoordinateOfOtherVehicle[0] and currentCoordinate[0] < \
                               currentCoordinateOfOtherVehicle[2]:
                           return [otherVehicle,abs(self.position[1]-otherVehicle.position[1])]

                       elif currentCoordinate[0] > currentCoordinateOfOtherVehicle[0] and currentCoordinate[2] < \
                               currentCoordinateOfOtherVehicle[0]:
                           return [otherVehicle,abs(self.position[1]-otherVehicle.position[1])]


                   elif self.direction == "eastDown" and otherVehicle.position[0] < self.position[0]:
                       if currentCoordinateOfOtherVehicle[1] > currentCoordinate[1] and currentCoordinateOfOtherVehicle[
                           1] < currentCoordinate[3]:
                           return [otherVehicle,abs(self.position[0]-otherVehicle.position[0])]

                       elif currentCoordinateOfOtherVehicle[3] > currentCoordinate[3] and \
                                       currentCoordinateOfOtherVehicle[3] < currentCoordinate[3]:
                           return [otherVehicle,abs(self.position[0]-otherVehicle.position[0])]

                       elif currentCoordinate[3] > currentCoordinateOfOtherVehicle[1] and currentCoordinate[1] < \
                               currentCoordinateOfOtherVehicle[3]:
                           return [otherVehicle,abs(self.position[0]-otherVehicle.position[0])]

                       elif currentCoordinate[1] > currentCoordinateOfOtherVehicle[1] and currentCoordinate[3] < \
                               currentCoordinateOfOtherVehicle[1]:
                           return [otherVehicle,abs(self.position[0]-otherVehicle.position[0])]


                   elif self.direction == "westUp" and otherVehicle.position[0] > self.position[0]:
                       if currentCoordinateOfOtherVehicle[1] > currentCoordinate[1] and currentCoordinateOfOtherVehicle[
                           1] < currentCoordinate[3]:
                           return [otherVehicle,abs(self.position[0]-otherVehicle.position[0])]

                       elif currentCoordinateOfOtherVehicle[3] > currentCoordinate[3] and \
                                       currentCoordinateOfOtherVehicle[3] < currentCoordinate[3]:
                           return [otherVehicle,abs(self.position[0]-otherVehicle.position[0])]

                       elif currentCoordinate[3] > currentCoordinateOfOtherVehicle[1] and currentCoordinate[1] < \
                               currentCoordinateOfOtherVehicle[3]:
                           return [otherVehicle,abs(self.position[0]-otherVehicle.position[0])]

                       elif currentCoordinate[1] > currentCoordinateOfOtherVehicle[1] and currentCoordinate[3] < \
                               currentCoordinateOfOtherVehicle[1]:
                           return [otherVehicle,abs(self.position[0]-otherVehicle.position[0])]
        else:
            return None

    def getDistanceToTrafficLight(self):
        lanePosition = trafficMap[self.direction]
        selfPosition = self.instantaneousPosition
        return math.hypot((lanePosition[0] - self.position[0]), (lanePosition[1] - self.position[1]))

    def pressAcceleration(self):
        if self.direction == 'southLeft':
            self.instantaneousAcceleration = self.driver.accelerationCoefficient * self.driver.getInstantaneousPressure(
                self)
            temp = self.instantaneousVelocity * timeUnit + self.instantaneousAcceleration * 0.5 * timeUnit*timeUnit  # ut+0.5at^2
            self.position[1] = self.position[1] - temp
            self.instantaneousVelocity = self.instantaneousAcceleration * timeUnit

        if self.direction == 'northRight':
            self.instantaneousAcceleration = self.driver.accelerationCoefficient * self.driver.getInstantaneousPressure(
                self)
            temp = self.instantaneousVelocity * timeUnit + self.instantaneousAcceleration * 0.5 * timeUnit * timeUnit  # ut+0.5at^2
            self.position[1] = self.position[1] + temp
            self.instantaneousVelocity = self.instantaneousAcceleration * timeUnit

        if self.direction == 'eastDown':
            self.instantaneousAcceleration = self.driver.accelerationCoefficient * self.driver.getInstantaneousPressure(
                self)
            temp = self.instantaneousVelocity * timeUnit + self.instantaneousAcceleration * 0.5 * timeUnit * timeUnit  # ut+0.5at^2
            self.position[0] = self.position[0] - temp
            self.instantaneousVelocity = self.instantaneousAcceleration * timeUnit

        if self.direction == 'westUp':
            self.instantaneousAcceleration = self.driver.accelerationCoefficient * self.driver.getInstantaneousPressure(self)
            temp = self.instantaneousVelocity * timeUnit + self.instantaneousAcceleration * 0.5 * timeUnit * timeUnit  # ut+0.5at^2
            self.position[0] = self.position[0] + temp
            self.instantaneousVelocity = self.instantaneousAcceleration * timeUnit

    def pressBrake(self, estimate):
        self.instantaneousVelocity=0
        self.instantaneousAcceleration=0
        self.isMoving=False




    # Initiates the movement of the vehicle
    def start(self):
        #print(self.position)
        if self.position[0]<-20 or self.position[0]>1320 or self.position[1]<-20 or self.position[1]>820:
            self.guiTimer.cancel()
            self.timer.cancel()

            if self.direction=="eastDown" and countOfVehicles["westUp"]>0:
                countOfVehicles["westUp"]-=1

            elif self.direction=="westUp" and countOfVehicles["eastDown"]>0:
                countOfVehicles["eastDown"]-=1

            elif self.direction == "northRight" and countOfVehicles["southLeft"]>0:
                countOfVehicles["southLeft"] -= 1

            elif self.direction=="southLeft" and countOfVehicles["northRight"]>0:
                countOfVehicles["northRight"]-=1


        else:
            self.pressAcceleration()
            behaviour=generateAllScore(self)

            if not self.hasToStop:
                self.timer=Timer(0.01, self.start)
                self.timer.start()



    def printVehicleInformation(self):
        print("Id: "+str(self.id)+" Direction: "+self.direction+" Type: "+self.type+" |Position: "+str(self.position)+" |Velocity: "+str(self.instantaneousVelocity)+" |Acceleration: "+str(self.instantaneousAcceleration)+" |Turn Left: "+str(self.turnLeft)+" |Turn Right: "+str(self.turnRight))
        print("\n")
        Timer(1,self.printVehicleInformation).start()


    def waitForGreenSignal(self):
        if self.direction==getAllowedDirection():
            self.hasToStop=False
            self.start()
            return
        else:
            self.Timer=Timer(1,self.waitForGreenSignal).start()
