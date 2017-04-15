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

lastPositionDictionary={}

#Stores the statistics of each vehicle
vehicleStatusMap={}

countOfVehicles={}
countOfVehicles["northRight"]=0
countOfVehicles["southLeft"]=0
countOfVehicles["westUp"]=0
countOfVehicles["eastDown"]=0

permanentCount={}
permanentCount["northRight"]=1
permanentCount["southLeft"]=1
permanentCount["westUp"]=1
permanentCount["eastDown"]=1

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
