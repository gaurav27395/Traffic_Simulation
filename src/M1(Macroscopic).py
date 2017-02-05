import random
from threading import Timer
from Tkinter import *

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
vehiclesCrossingPerTimerExpiry=25

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
    if globals()[queueVariable]>vehiclesCrossingPerTimerExpiry:
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


canvas = Canvas(width=500, height=500, bg='gray11')  
canvas.pack(expand=YES, fill=BOTH)                
canvas.create_rectangle(200, 200, 300, 300, fill='gray26')
canvas.create_rectangle(25, 25, 175, 175, fill='green4')
canvas.create_rectangle(325, 25, 475, 175, fill='green4')
canvas.create_rectangle(25, 325, 175, 475, fill='green4')
canvas.create_rectangle(325, 325, 475, 475, fill='green4')
canvas.create_rectangle(200, 0, 300, 200, fill='grey') #North
canvas.create_rectangle(0, 200, 200, 300, fill='grey') #West
canvas.create_rectangle(300, 200, 500, 300, fill='grey') #East
canvas.create_rectangle(200, 300, 300, 500, fill='grey') #South
west = Label(text="West")
west.place(x=20,y=240)
east = Label(text="East")
east.place(x=450,y=240)
north = Label(text="North")
north.place(x=230,y=20)
south = Label(text="South")
south.place(x=230,y=480)
def line_continuous():
	global westQueueLength,northQueueLength,eastQueueLength,southQueueLength;
	
	canvas.create_rectangle(0, 200, 200, 300, fill='gray64') #West
	canvas.create_line(200, 250, 200-westQueueLength, 250, width=50, fill='blue')
	west1 = Label(text=""+str(westQueueLength))
	west1.place(x=120,y=240)
	canvas.create_rectangle(200, 0, 300, 200, fill='gray64') #North
	canvas.create_line(250, 200, 250, 200-northQueueLength, width=50, fill='orange')
	north1 = Label(text=""+str(northQueueLength))
	north1.place(x=240,y=80)
	canvas.create_rectangle(300, 200, 500, 300, fill='gray64') #East
	canvas.create_line(300, 250, 300+eastQueueLength, 250, width=50, fill='navy')
	east1 = Label(text=""+str(eastQueueLength))
	east1.place(x=350,y=240)
	canvas.create_rectangle(200, 300, 300, 500, fill='gray64') #South
	canvas.create_line(250, 300, 250, 300+southQueueLength, width=50, fill='brown')
	south1 = Label(text=""+str(southQueueLength))
	south1.place(x=240,y=400)
	Timer(0.5,line_continuous).start()

#Begin Simulation Process

#Create 3 different Timer objects for handling 3 different timeouts.
Timer(trafficTimeout,changeDirection).start()
Timer(addTimeout,addToQueue).start()
Timer(removeTimeout,removeFromQueue).start()
printTimer=Timer(1,printInformation).start()
Timer(0.5,line_continuous).start()
mainloop()
