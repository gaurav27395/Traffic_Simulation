from Microscopic.Environment import *

def generateAllScore(vehicle):
    carfollowingscore = generateCarFollowingScore(vehicle)
    roadfollowingscore = 0
    trafficlightscore = generateTrafficLightScore(vehicle)
    changedirectionscore = generateChangeDirectionScore(vehicle)
    emergencybrakingscore = generateEmergencyBrakingScore(vehicle)
    scoretuple = [carfollowingscore, roadfollowingscore, trafficlightscore, changedirectionscore, emergencybrakingscore]
    maxscore = max(scoretuple)

    if maxscore == carfollowingscore:
        carFollowExecute(vehicle)
        return "Car Following executed"

    if maxscore == trafficlightscore:
        trafficLightExecute(vehicle)
        return "Traffic Light executed"

    if maxscore == changedirectionscore:
        changeDirectionExecute(vehicle)
        print("Going inside Change Direction")
        return "Change Direction executed"

    if maxscore == emergencybrakingscore:
        emergencyBrakingExecute(vehicle)
        return "emergency braking executed"


# Car Following Score
def generateCarFollowingScore(vehicle):
    distance = vehicle.getInformationOfNearestVehicle()[1]

    if distance >= 50:
        return 0
    elif distance >= 40 and distance < 50:
        return 2.5
    elif distance >= 30 and distance < 40:
        return 5
    elif distance >= 20 and distance < 30:
        return 7.5
    elif distance <= 20:
        return 8
    elif distance < 10:
        return 0


# Traffic light Score
def generateTrafficLightScore(vehicle):
    trafficlight_distance = vehicle.getDistanceToTrafficLight()

    if trafficlight_distance <= 10:
        return 10
    else:
        return 0


def generateChangeDirectionScore(vehicle):
    distance = vehicle.getDistanceToTrafficLight()
    score=0

    if distance <= 1 and vehicle.direction==getAllowedDirection():
        score= 11
    else:
        score= 0
    print("Traffic score was calculated: "+str(distance)+" "+str(score))
    return score




# Emergency Braking Score:
def generateEmergencyBrakingScore(vehicle):
    distance = vehicle.getInformationOfNearestVehicle()

    if distance[1] < 2:
        return 10
    else:
        return 0


def carFollowExecute(vehicle):
    # distance = vehicle.getDistancetoNearestVehicle()
    # coordinates = vehicle.getCoordinatetoNearestVehicle()
    speed = vehicle.getInformationOfNearestVehicle()[1]
    vehicle.speed = speed


def trafficLightExecute(vehicle):
    if vehicle.direction != getAllowedDirection():
        vehicle.hasToStop = True
        vehicle.pressBrake(vehicle.getDistanceToTrafficLight())
        vehicle.waitForGreenSignal()



def emergencyBrakingExecute(vehicle):
    vehicle.applyBrake()

def changeDirectionExecute(vehicle):
<<<<<<< HEAD
     if vehicle.turnLeft:
            vehicle.position[0], vehicle.position[1] = vehicle.position[1], vehicle.position[0]

     elif vehicle.turnRight:
            vehicle.position[0], vehicle.position[1] = -vehicle.position[1], -vehicle.position[0]

=======
        if vehicle.turnLeft:
            vehicle.position[0], vehicle.position[1] = vehicle.position[1], vehicle.position[0]
        
        elif vehicle.turnRight:
            vehicle.position[0], vehicle.position[1] = -vehicle.position[1], -vehicle.position[0]


>>>>>>> 1b7d239b6e1425702e6acc720d9927d8483866e0
