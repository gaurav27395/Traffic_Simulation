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
southLeftTrafficLight=(-5,-10)
eastDownTrafficLight=(10,-5)
westUpTrafficLight=(-10,5)


trafficMap={
"northRight":(5,10),
"southLeft":(-5,-10),
"eastDown":(10,-5),
"westUp":(-10,5)
}

#Stores the statistics of each vehicle
vehicleStatusMap={}

#Add or update vehicles.
def addVehicleToEnvironment(id,position):
    vehicleStatusMap[id]=position

#Return the vehicle position.
def getEnvironmentInformation():
    return vehicleStatusMap

def getAllowedDirection():
    file=open('signal.txt')
    allowedDirection=file.read()
    file.close()
    return allowedDirection