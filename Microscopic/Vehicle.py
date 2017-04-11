# This module represents a vehicle and its different properties
from Environment import *
from Driver import *
from Behaviour import *
from TrafficLight import *
import math

timeUnit = 0.3


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
        self.vehicleTypeMap = {"bike": 1, "car": 2, "truck": 3}
        self.hasToStop=False

        if direction == "northRight" or direction == "eastDown":
            self.instantaneousPosition = random.randint(350,400)

        elif direction == "southLeft" or direction == "westUp":
            self.instantaneousPosition = random.randint(-400,-350)

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
        speedOfNearestVehicle=0
        leftCoordinate = [(self.position[0] - self.vehicleTypeMap[self.type] / 2),
                          (self.position[1] + self.vehicleTypeMap[self.type] / 2)]
        rightCoordinate = [(self.position[0] + self.vehicleTypeMap[self.type] / 2),
                           (self.position[1] + self.vehicleTypeMap[self.type] / 2)]
        upLeftCoordinate = [leftCoordinate[0], leftCoordinate[1] + self.visibilityRectangle]
        upRightCoordinate = [rightCoordinate[0], rightCoordinate[1] + self.visibilityRectangle]
        carDictionary = getEnvironmentInformation()
        nearestVehicle = [0, 0]
        distance = 400

        for key, value in carDictionary.items():
            if (value.position[0] > leftCoordinate[0] and value.position[0] < rightCoordinate[0]) and (
                    value.position[1] > rightCoordinate[1] and value.position[1] < upRightCoordinate[1]):
                if math.hypot((value.position[0] - self.position[0]),
                              (value.position[1] - self.position[1])) < distance:
                    distance = math.hypot((value.position[0] - self.position[0]),
                                          (value.position[1] - self.position[1]))
                    nearestVehicle[0] = value.position[0]
                    nearestVehicle[1] = value.position[1]
                    speedOfNearestVehicle = value.instantaneousVelocity
        return [nearestVehicle, distance,speedOfNearestVehicle]

    def getDistanceToTrafficLight(self):
        lanePosition = trafficMap[self.direction]
        selfPosition = self.instantaneousPosition
        return math.hypot((lanePosition[0] - self.position[0]), (lanePosition[1] - self.position[1]))

    def pressAcceleration(self):
        if self.direction == 'southLeft':
            self.instantaneousAcceleration = self.driver.accelerationCoefficient * self.driver.getInstantaneousPressure(
                self)
            temp = self.instantaneousVelocity * timeUnit + self.instantaneousAcceleration * 0.5 * timeUnit*timeUnit  # ut+0.5at^2
            self.position[1] = self.position[1] + temp
            self.instantaneousVelocity = self.instantaneousAcceleration * timeUnit

        if self.direction == 'northRight':
            self.instantaneousAcceleration = self.driver.accelerationCoefficient * self.driver.getInstantaneousPressure(
                self)
            temp = self.instantaneousVelocity * timeUnit + self.instantaneousAcceleration * 0.5 * timeUnit * timeUnit  # ut+0.5at^2
            self.position[1] = self.position[1] - temp
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

    # Initiates the movement of the vehicle
    def start(self):
        self.pressAcceleration()
        behaviour=generateAllScore(self)

        if not self.hasToStop:
            Timer(1, self.start).start()



    def printVehicleInformation(self):
        print("Id: "+str(self.id)+" Direction: "+self.direction+" Type: "+self.type+" |Position: "+str(self.position)+" |Velocity: "+str(self.instantaneousVelocity)+" |Acceleration: "+str(self.instantaneousAcceleration))
        print("\n")
        Timer(1,self.printVehicleInformation).start()


    def waitForGreenSignal(self):
        if self.direction==getAllowedDirection():
            self.hasToStop=False
            self.start()
            return
        else:
            Timer(1,self.waitForGreenSignal).start()
