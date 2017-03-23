#This file implements the spatial network ofraods and traffic intersections.
#Every corner in the road has been assigned a fixed cartesian co-ordinate.
#Every traffic light has been assigned a fixed cartesian co-ordinate.
#The module also stores the position of every vehicle.
#Updation or addition  of position of a vehicle is also don in this module.
#Origin has been defined at the geometric centre of the system.

northRightCorner=(10,400)
northLeftCorner=(-10,400)
southLeftCorner=(10,-400)
southRightCorner=(-10,-400)
eastUpCorner=(400,10)
eastDownCorner=(400,-10)
westUpCorner=(-400,10)
westDownCorner=(-400,-10)
origin=(0,0)

northRightTrafficLight=(5,10)
northLeftTrafficLight=(-5,10)
southLeftTrafficLight=(-5,-10)
southRightTrafficLight=(5,-10)
eastUpTrafficLight=(10,5)
eastDownTrafficLight=(10,-5)
westUpTrafficLight=(-10,5)
westDownTrafficLight=(-10,-5)


trafficMap={"northRight":(5,10),
"northLeft":(-5,10),
"southLeft":(-5,-10),
"southRight":(5,-10),
"eastUp":(10,5),
"eastDown":(10,-5),
"westUp":(-10,5),
"westDown":(-10,-5)
}

#Tells the position of each vehicle
vehiclePosition={}

#Add or update vehicles.
def addOrUpdateVehicle(id,position):
    vehiclePosition[id]=position

#Return the vehicle position.
def getVehiclePositions():
    return vehiclePosition

