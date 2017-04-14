from Microscopic.Environment import *
from threading import Timer

def generateAllScore(vehicle):
    carfollowingscore = generateCarFollowingScore(vehicle)
    roadfollowingscore = 0
    trafficlightscore = generateTrafficLightScore(vehicle)
    changedirectionscore = generateChangeDirectionScore(vehicle)
    emergencybrakingscore = generateEmergencyBrakingScore(vehicle)
    scoretuple = [carfollowingscore, roadfollowingscore, trafficlightscore, changedirectionscore, emergencybrakingscore]
    maxscore = max(scoretuple)

    # if maxscore == carfollowingscore:
    #     carFollowExecute(vehicle)
    #     return "Car Following executed"

    if maxscore == trafficlightscore:
        trafficLightExecute(vehicle)
        return "Traffic Light executed"

    if maxscore == changedirectionscore:
        changeDirectionExecute(vehicle)
        return "Change Direction executed"

    if maxscore == emergencybrakingscore:
        emergencyBrakingExecute(vehicle)
        return "emergency braking executed"


# Car Following Score
def generateCarFollowingScore(vehicle):
    distance = vehicle.getInformationOfNearestVehicle()[1]

    if distance <= 300 and distance > 150:
        return 9
    else:
        return 0


# Traffic light Score
def generateTrafficLightScore(vehicle):
    trafficlight_distance = vehicle.getDistanceToTrafficLight()

    if trafficlight_distance <= 100:
        return 10
    else:
        return 0


def generateChangeDirectionScore(vehicle):
    distance = vehicle.getDistanceToTrafficLight()
    score = 0

    if distance <= 50 and vehicle.direction == getAllowedDirection() and (vehicle.turnLeft or vehicle.turnRight):
        score = 11
    else:
        score = 0
    return score


# Emergency Braking Score:
def generateEmergencyBrakingScore(vehicle):
    distance = vehicle.getInformationOfNearestVehicle()

    if distance[1] < 2:
        return 10
    else:
        return 0


def carFollowExecute(vehicle):
    speed = vehicle.getInformationOfNearestVehicle()[1]
    vehicle.speed = speed


def trafficLightExecute(vehicle):
    if vehicle.direction != getAllowedDirection() and vehicle.getDistanceToTrafficLight()<50:
        vehicle.hasToStop = True
        vehicle.pressBrake(vehicle.getDistanceToTrafficLight())
        vehicle.waitForGreenSignal()


def emergencyBrakingExecute(vehicle):
    vehicle.applyBrake()


def changeDirectionExecute(vehicle):
    if vehicle.turnLeft:
        if vehicle.direction == "southLeft":
            if vehicle.position[1]<430:
                vehicle.direction="eastDown"
                vehicle.turnLeft=False
                vehicle.turnRight=False

    if vehicle.turnLeft:
        if vehicle.direction == "northRight":
            if vehicle.position[1]>330:
                vehicle.direction="westUp"
                vehicle.turnLeft = False
                vehicle.turnRight = False

    if vehicle.turnLeft:
        if vehicle.direction == "westUp":
            if vehicle.position[0]>560:
                vehicle.direction="southLeft"
                vehicle.turnLeft = False
                vehicle.turnRight = False
    if vehicle.turnLeft:
        if vehicle.direction == "eastDown":
            if vehicle.position[0]<710:
                vehicle.direction="northRight"
                vehicle.turnLeft = False
                vehicle.turnRight = False

    if vehicle.turnRight:
        if vehicle.direction == "southLeft":
            if vehicle.position[1] < 430:
                vehicle.direction = "westUp"
                vehicle.turnLeft = False
                vehicle.turnRight = False

    if vehicle.turnRight:
        if vehicle.direction == "northRight":
            if vehicle.position[1] > 330:
                vehicle.direction = "eastDown"
                vehicle.turnLeft = False
                vehicle.turnRight = False

    if vehicle.turnRight:
        if vehicle.direction == "westUp":
            if vehicle.position[0] > 560:
                vehicle.direction = "northRight"
                vehicle.turnLeft = False
                vehicle.turnRight = False

    if vehicle.turnRight:
        if vehicle.direction == "eastDown":
            if vehicle.position[0] < 710:
                vehicle.direction = "southLeft"
                vehicle.turnLeft = False
                vehicle.turnRight = False
