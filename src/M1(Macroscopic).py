import random
from threading import Timer

#Current Direction from which vehicles can move
allowedDirection="north"

#Respective lengths of the queue
eastQueueLength=0
westQueueLength=0
northQueueLength=0
southQueueLength=0

#Paramters to be used while changing the direction when the traffic timer expires.
directionArray=["north","east","south","west"]
directionIndex=0
directionDictionary={"north":"northQueueLength","east":"eastQueueLength","west":"westQueueLength","south":"southQueueLength"}

#The time for which the signal remains green for one direction
trafficTimeout=5

#The corresponding timers for adding and removing from a queue
removeTimeout=3
addTimeout=1

#The distribution being used to calculate the inter-arrival time of vehicles
trafficDistribution=None

#The number of vehicles which have crossed and left the respective queue whenever the timer expires.
#Caution: This is not calucluated per phase cycle rather per timer expiry.
vehiclesCrossingPerTimerExpiry=2

#Initially all the directions will be allocated a random queue length between 5-10
eastQueueLength=random.randint(5,10)
westQueueLength=random.randint(5,10)
northQueueLength=random.randint(5,10)
southQueueLength=random.randint(5,10)

#The function adds a vehicle to the respective queue whenever the vehicle arrives at the intersection.
def addToQueue():
    globals()["eastQueueLength"]+=1
    globals()["westQueueLength"]+=1
    globals()["southQueueLength"]+=1
    globals()["westQueueLength"]+=1
    Timer(addTimeout,addToQueue).start()


#The function removes a fixed number of vehicles whenever the timer expires
def removeFromQueue():
    queueVariable=directionDictionary[allowedDirection]

    #If vehicles are pressent then make them cross the intersection
    if globals()[queueVariable]>=0:
        globals()[queueVariable]-=vehiclesCrossingPerTimerExpiry

    Timer(removeTimeout,removeFromQueue).start()

#The function changes the allowed direction whenever the traffic timer expires.
def changeDirection():
    print(directionIndex)
    globals()["directionIndex"]=(directionIndex+1)%4
    globals()["allowedDirection"]=directionArray[directionIndex]
    Timer(trafficTimeout,changeDirection).start()

#Prints the current information
def printInformation():
    print("***************************************************************")
    print("Allowed Direction: ",allowedDirection)
    print("East Queue Length: ",eastQueueLength)
    print("West Queue Length: ", westQueueLength)
    print("South Queue Length: ", southQueueLength)
    print("North Queue Length: ", northQueueLength)
    print("***************************************************************\n")
    Timer(1,printInformation).start()

#Begin Simulation Process

#Create 3 different Timer objects for handling 3 different timeouts.
Timer(trafficTimeout,changeDirection).start()
Timer(addTimeout,addToQueue).start()
Timer(removeTimeout,removeFromQueue).start()
printTimer=Timer(1,printInformation).start()
