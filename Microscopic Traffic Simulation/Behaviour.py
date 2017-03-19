import math

def generateAllScore(vehicle):
    carfollowingscore= generateCarFollowingScore(vehicle);
    roadfollowingscore = generateRoadFollowingScore(vehicle);
    trafficlightscore = generateTrafficLightScore(vehicle);
    changedirectionscore = generateChangeDirectionScore(vehicle);
    emergencybrakingscore = generateEmergencyBrakingScore(vehicle);

def generateCarFollowingScore(vehicle):
    distance=vehicle.getDistancetoNearestVehicle();
    if(distance>= 50):
        return 0
    if (distance>= 40 and distance< 50):
        return 2.5
    if (distance>= 30 and distance< 40):
        return 5
    if (distance>= 20 and distance< 30):
        return 7.5
    if (distance <= 20):
        return 10

def generateRoadFollowingScore():
    print()

def generateTrafficLightScore(vehicle):
    trafficlight_position=vehicle.getLaneSignalPosition();
    trafficlight_diatance = math.hypot(trafficlight_position[0] - vehicle.x, trafficlight_position[1] - vehicle.y)
    if(trafficlight_diatance<=10 and vehicle.getDistancetoNearestVehicle()==0 ):
        return 10;
    else:
        return 0;

def generateChangeDirectionScore(vehicle):
    print()

def generateEmergencyBrakingScore():
    print()

def carFollowExecute(vehicle):
    #distance = vehicle.getDistancetoNearestVehicle();
    #coordinates = vehicle.getCoordinatetoNearestVehicle();
    speed = vehicle.getSpeedtoNearestVehicle();
    vehicle.speed=speed;

def trafficLightExecute(vehicle):
    if(vehicle.cuurentLane.trafficsignal=="Red"):
        vehicle.stop();

# Emergency Braking Score:

def emergencyBrakingScore(vehicle):
	for id in positionMap:
		distance = vehicle.getDistanceToNearestVehicle()
		if distance < 2:
			return 10
		else 
			return 0

#Genrate Change Direction Score

def generateChangeDirectionScore(vehicle):
	position = vehicle.getLaneSignalPosition()

	if vehicle.position[1]==position[1] and (vehicle.turnLeft or vehcle.turnRight):
		return 10

	else 
		return 0

def emergencyDirectionExecute(vehicle):
	vehicle.stop();

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



