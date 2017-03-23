import math
def generateAllScore(vehicle):

    carfollowingscore= generateCarFollowingScore(vehicle)
    roadfollowingscore = 0
    trafficlightscore = generateTrafficLightScore(vehicle)
    changedirectionscore = generateChangeDirectionScore(vehicle)
    emergencybrakingscore = generateEmergencyBrakingScore(vehicle)
    scoretuple=[carfollowingscore,roadfollowingscore,trafficlightscore, changedirectionscore,emergencybrakingscore]
    maxscore=max(scoretuple)


    if(maxscore==carfollowingscore):
        carFollowExecute(vehicle)
        return ("Car Following executed")

    if(maxscore==trafficlightscore):
        trafficLightExecute(vehicle)
        return("Traffic Light executed")

    if(maxscore==changedirectionscore):
        generateChangeDirectionExecute(vehicle)
        return("Chenge Direction executed")

    if(maxscore==emergencybrakingscore):
        emergencyBrakingExecute(vehicle)
        return("emergency braking executed")

# Car Following Score
def generateCarFollowingScore(vehicle):
    distance=vehicle.getDistancetoNearestVehicle()

    if(distance[1]>= 50):
        return 0
    if (distance[1]>= 40 and distance[1]< 50):
        return 2.5
    if (distance[1]>= 30 and distance[1]< 40):
        return 5
    if (distance[1]>= 20 and distance[1]< 30):
        return 7.5
    if (distance[1] <= 20):
        return 8

# Traffic light Score
def generateTrafficLightScore(vehicle):
    trafficlight_distance=vehicle.getLaneSignalPosition()

    if(trafficlight_distance<=10 and vehicle.getDistancetoNearestVehicle()[1]>=10 ):
        return 10
    else:
        return 0

def generateChangeDirectionScore(vehicle):
	distance = vehicle.getLaneSignalPosition()

	if distance==0 and (vehicle.turnLeft or vehicle.turnRight):
		return 9
	else:
		return 0

# Emergency Braking Score:
def generateEmergencyBrakingScore(vehicle):
	distance = vehicle.getDistancetoNearestVehicle()

	if distance[1] < 2:
		return 10
	else:
		return 0

def carFollowExecute(vehicle):
    #distance = vehicle.getDistancetoNearestVehicle()
    #coordinates = vehicle.getCoordinatetoNearestVehicle()
    speed = vehicle.speedOfNearestVehicle
    vehicle.speed=speed

def trafficLightExecute(vehicle):
    if(vehicle.currentLane=="Red"):
        vehicle.stop()

def generateChangeDirectionExecute(vehicle):
	lane = vehicle.currentLane()
	direction = vehicle.getDirection()
	if lane == 'south' and direction == 'left' :
		vehicle.position[0] , vehicle.position[1] = vehicle.position[1] , vehicle.position[0]
	elif lane == 'south' and direction == 'right' :
		vehicle.position[0] , vehicle.position[1] = vehicle.position[1] , vehicle.position[0]
	elif lane == 'north' and  direction == 'right' :
		vehicle.position[0] , vehicle.position[1] = vehicle.position[1] , vehicle.position[0]
	elif lane == 'north' and direction == 'left' :
		vehicle.position[0] , vehicle.position[1] = vehicle.position[1] , vehicle.position[0]
	elif lane == 'east' and direction == 'left' :
		vehicle.position[0] , vehicle.position[1] = vehicle.position[1] , vehicle.position[0]
	elif lane == 'east' and direction == 'right' :
		vehicle.position[0] , vehicle.position[1] = vehicle.position[1] , vehicle.position[0]
	elif lane == 'west' and direction == 'right' :
		vehicle.position[0] , vehicle.position[1] = vehicle.position[1] , vehicle.position[0]
	elif lane == 'west' and direction == 'left' :
		vehicle.position[0] , vehicle.position[1] = vehicle.position[1] , vehicle.position[0]

def emergencyBrakingExecute(vehicle):
	vehicle.stop()
