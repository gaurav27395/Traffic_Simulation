from Microscopic.Environment import *
from threading import Timer
import time
import random
def generateAllScore(vehicle):
    trafficlightscore = generateTrafficLightScore(vehicle)
    changedirectionscore = generateChangeDirectionScore(vehicle)
    overtakingscore = generateovertakingScore(vehicle)

    scoretuple = [overtakingscore, trafficlightscore,changedirectionscore]
    maxscore = max(scoretuple)


    if maxscore == trafficlightscore:
        trafficLightExecute(vehicle)
        return "Traffic Light executed"

    if maxscore == changedirectionscore:
        changeDirectionExecute(vehicle)
        return "Change Direction executed"

    if maxscore == overtakingscore:
        overtakingExecute(vehicle)
        return "emergency braking executed"

def generateTrafficLightScore(vehicle):
    trafficlight_distance = vehicle.getDistanceToTrafficLight()

    if trafficlight_distance <= 40 :
        return 12
    else:
        return 0


def generateChangeDirectionScore(vehicle):
    distance = vehicle.getDistanceToTrafficLight()
    score = 0

    if distance <= 300  and (vehicle.turnLeft or vehicle.turnRight):
        score = 11
    else:
        score = 0
    return score


# Emergency Braking Score:
def generateovertakingScore(vehicle):
    information=vehicle.getInformationOfNearestVehicle()

    if information:
        distance=information[1]
        otherVehicle = information[0]

        if distance < 20 :

            return 14
        else:
            return 0
    else:
        return 0


def trafficLightExecute(vehicle):
    if vehicle.direction != getAllowedDirection() and vehicle.getDistanceToTrafficLight()<50 and (not vehicle.doNotStop):
        vehicle.entryTime=time.time()
        vehicle.hasToStop = True
        vehicle.pressBrake(vehicle.getDistanceToTrafficLight())
        vehicle.waitForGreenSignal()
        vehicle.isMoving=True
        vehicle.exitTime=time.time()
        vehicle.doNotStop=True


def overtakingExecute(vehicle):
    if vehicle.direction=="northRight":
            if vehicle.position[0]<=700:
                vehicle.position[0]+=4
                getCanvasReference().move(vehicle.guiRectangle, 4, 0)
            else:
                vehicle.position[0] -= 4
                getCanvasReference().move(vehicle.guiRectangle, -4, 0)

    if vehicle.direction == "southLeft":
            if vehicle.position[0]<=600:
                vehicle.position[0]+=4
                getCanvasReference().move(vehicle.guiRectangle, 4, 0)
            else:
                vehicle.position[0] -= 4
                getCanvasReference().move(vehicle.guiRectangle, -4, 0)

    if vehicle.direction=="eastDown":
            if vehicle.position[1]<=420:

                vehicle.position[1]+=4
                getCanvasReference().move(vehicle.guiRectangle, 0, -4)
            else:
                vehicle.position[1] -= 4
                getCanvasReference().move(vehicle.guiRectangle, 0, -4)

    if vehicle.direction=="westUp":
            if vehicle.position[1]<=340:
                vehicle.position[1]+=4
                getCanvasReference().move(vehicle.guiRectangle, 0, 4)
            else:
                vehicle.position[1] -= 4
                getCanvasReference().move(vehicle.guiRectangle, 0, -4)
    return


def changeDirectionExecute(vehicle):
    if vehicle.turnLeft:
        if vehicle.direction == "southLeft":
            if vehicle.position[1]<430:
                vehicle.direction="eastDown"
                vehicle.turnLeft=False
                vehicle.turnRight=False
                countOfVehicles["southLeft"]-=1
                countOfVehicles["westUp"] += 1



    if vehicle.turnLeft:
        if vehicle.direction == "northRight":
            if vehicle.position[1]>330:
                vehicle.direction="westUp"
                vehicle.turnLeft = False
                vehicle.turnRight = False
                countOfVehicles["northRight"] -= 1
                countOfVehicles["eastDown"] += 1

    if vehicle.turnLeft:
        if vehicle.direction == "westUp":
            if vehicle.position[0]>560:
                vehicle.direction="southLeft"
                vehicle.turnLeft = False
                vehicle.turnRight = False
                countOfVehicles["westUp"] -= 1
                countOfVehicles["northRight"] += 1

    if vehicle.turnLeft:
        if vehicle.direction == "eastDown":
            if vehicle.position[0]<710:
                vehicle.direction="northRight"
                vehicle.turnLeft = False
                vehicle.turnRight = False
                countOfVehicles["eastDown"] -= 1
                countOfVehicles["southLeft"] += 1

    if vehicle.turnRight:
        if vehicle.direction == "southLeft":
            if vehicle.position[1] < 360:
                vehicle.direction = "westUp"
                vehicle.turnLeft = False
                vehicle.turnRight = False
                countOfVehicles["southLeft"] -= 1
                countOfVehicles["eastDown"] += 1

    if vehicle.turnRight:
        if vehicle.direction == "northRight":
            if vehicle.position[1] > 400:
                vehicle.direction = "eastDown"
                vehicle.turnLeft = False
                vehicle.turnRight = False
                countOfVehicles["northRight"] -= 1
                countOfVehicles["westUp"] += 1

    if vehicle.turnRight:
        if vehicle.direction == "westUp":
            if vehicle.position[0] > 700:
                vehicle.direction = "northRight"
                vehicle.turnLeft = False
                vehicle.turnRight = False
                countOfVehicles["westUp"] -= 1
                countOfVehicles["southLeft"] += 1

    if vehicle.turnRight:
        if vehicle.direction == "eastDown":
            if vehicle.position[0] < 600:
                vehicle.direction = "southLeft"
                vehicle.turnLeft = False
                vehicle.turnRight = False
                countOfVehicles["eastDown"] -= 1
                countOfVehicles["northRight"] += 1
