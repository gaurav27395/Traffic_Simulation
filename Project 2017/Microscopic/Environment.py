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
totalVehicleCount=0
Timing={}
Timing["northRight"]=0
Timing["southLeft"]=0
Timing["westUp"]=0
Timing["eastDown"]=0

smartTiming={}
smartTiming["northRight"]=0
smartTiming["southLeft"]=0
smartTiming["westUp"]=0
smartTiming["eastDown"]=0
lastPositionDictionary={}
canvasReference=None

#Stores the statistics of each vehicle
vehicleStatusMap={}

useSmartTrafficLight=False

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

smartPermanentCount={}
smartPermanentCount["northRight"]=1
smartPermanentCount["southLeft"]=1
smartPermanentCount["westUp"]=1
smartPermanentCount["eastDown"]=1

totalCount={}
totalCount["northRight"]=1
totalCount["southLeft"]=1
totalCount["westUp"]=1
totalCount["eastDown"]=1

#Add or update vehicles.
def addVehicleToEnvironment(id,position):
    vehicleStatusMap[id]=position

#Return the vehicle position.
def getEnvironmentInformation():
    return vehicleStatusMap

def sendCanvasReference(canvas):
    global canvasReference
    canvasReference=canvas

def getAllowedDirection():
    file=open('signal.txt')
    allowedDirection=file.read()
    file.close()
    return allowedDirection

def getCanvasReference():
    return canvasReference