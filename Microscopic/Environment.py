#This file implements the spatial network ofraods and traffic intersections.
#Every corner in the road has been assigned a fixed cartesian co-ordinate.
#Every traffic light has been assigned a fixed cartesian co-ordinate.
#The module also stores the position of every vehicle.
#Updation or addition  of position of a vehicle is also don in this module.
#Origin has been defined at the geometric centre of the system.

trafficMap={
"northRight":(700,300),
"southLeft":(600,460),
"eastDown":(750,420),
"westUp":(550,340)
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
