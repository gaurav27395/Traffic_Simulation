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
    if(maxscore==trafficlightscore):
    	trafficLightExecute(vehicle)
    if(maxscore==changedirectionscore):
    	generateChangeDirectionExecute(vehicle)
    if(maxscore==emergencybrakingscore):
    	emergencyBrakingExecute(vehicle)

# Car Following Score
def generateCarFollowingScore(vehicle):
    distance=vehicle.getDistancetoNearestVehicle()
    if(distance>= 50):
        return 0
    if (distance>= 40 and distance< 50):
        return 2.5
    if (distance>= 30 and distance< 40):
        return 5
    if (distance>= 20 and distance< 30):
        return 7.5
    if (distance <= 20):
        return 8

# Traffic light Score
def generateTrafficLightScore(vehicle):
    trafficlight_position=vehicle.getLaneSignalPosition()
    trafficlight_diatance = math.hypot(trafficlight_position[0] - vehicle.position[0], trafficlight_position[1] - vehicle.position[1])
    if(trafficlight_diatance<=10 and vehicle.getDistancetoNearestVehicle()>=10 ):
        return 10
    else:
        return 0

def generateChangeDirectionScore(vehicle):
	position = vehicle.getLaneSignalPosition()

	if vehicle.position[1]==position[1] and (vehicle.turnLeft or vehicle.turnRight):
		return 9
	else:
		return 0

# Emergency Braking Score:
def generateEmergencyBrakingScore(vehicle):
	distance = vehicle.getDistanceToNearestVehicle()

	if distance < 2:
		return 10
	else:
		return 0

def carFollowExecute(vehicle):
    #distance = vehicle.getDistancetoNearestVehicle()
    #coordinates = vehicle.getCoordinatetoNearestVehicle()
    speed = vehicle.getSpeedtoNearestVehicle()
    vehicle.speed=speed

def trafficLightExecute(vehicle):
    if(vehicle.cuurentLane.trafficsignal=="Red"):
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
