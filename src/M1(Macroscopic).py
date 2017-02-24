import random
from threading import Timer
from Tkinter import *
import distribution as dis

#Current Direction from which vehicles can move
allowedDirection="north"

#Respective lengths of the queue
eastQueueLength=0
westQueueLength=0
northQueueLength=0
southQueueLength=0

#Arrival times in all the direction.
arrival_east=0
arrival_west=0
arrival_north=0
arrival_south=0

#Paramters to be used while changing the direction when the traffic timer expires.
directionArray=["north","east","south","west"]
directionIndex=0
directionDictionary={"north":"northQueueLength","east":"eastQueueLength","west":"westQueueLength","south":"southQueueLength"}

#The time for which the signal remains green for one direction
trafficTimeout=6

#The corresponding timers for adding and removing from a queue
removeTimeout=2
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
    
#Here in arrival_east function we'll generate inter-arrival time and no. of cars on an arrival time
def arrival_east_fn():
    scale=3.4
    iat=dis.exponential_function(scale,1)[0]
    cars=dis.poisson_function(4,1)[0]
    global arrival_east,eastQueueLength
    eastQueueLength+=cars
    arrival_east+=iat
    Timer(arrival_east,arrival_east_fn).start()

def arrival_west_fn():
    scale=3.4
    iat=dis.exponential_function(scale,1)[0]
    cars=dis.poisson_function(4,1)[0]
    global arrival_west,westQueueLength
    westQueueLength+=cars
    arrival_west+=iat
    Timer(arrival_west,arrival_west_fn).start()

def arrival_north_fn():
    scale=3.4
    iat=dis.exponential_function(scale,1)[0]
    cars=dis.poisson_function(4,1)[0]
    global arrival_north,northQueueLength
    northQueueLength+=cars
    arrival_north+=iat
    Timer(arrival_north,arrival_north_fn).start()

def arrival_south_fn():
    scale=3.4
    iat=dis.exponential_function(scale,1)[0]
    cars=dis.poisson_function(4,1)[0]
    global arrival_south,southQueueLength
    southQueueLength+=cars
    arrival_south+=iat
    Timer(arrival_south,arrival_south_fn).start()    
    



#The function removes a fixed number of vehicles whenever the timer expires
def removeFromQueue():
    queueVariable=directionDictionary[allowedDirection]
    global vehiclesCrossingPerTimerExpiry
    vehiclesCrossingPerTimerExpiry=dis.poisson_function(3,1)[0]

    #If vehicles are pressent then make them cross the intersection
    if globals()[queueVariable]>=vehiclesCrossingPerTimerExpiry:
        globals()[queueVariable]-=vehiclesCrossingPerTimerExpiry

    Timer(removeTimeout,removeFromQueue).start()

#The function changes the allowed direction whenever the traffic timer expires.
def changeDirection():
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
    Timer(2,printInformation).start()


canvas = Canvas(width=1300, height=800, bg='gray11')  
canvas.pack(expand=YES, fill=BOTH)                
canvas.create_rectangle(550, 300, 750, 460, fill='gray26')
canvas.create_rectangle(0, 0, 550, 300, fill='green4')
canvas.create_rectangle(0, 460, 550, 800, fill='green4')
canvas.create_rectangle(750, 460, 1300, 800, fill='green4')
canvas.create_rectangle(750, 0, 1300, 300, fill='green4')
canvas.create_rectangle(550, 0, 750, 300, fill='grey') #North
canvas.create_rectangle(0, 300, 550, 460, fill='grey') #West
canvas.create_rectangle(550, 460, 750, 800, fill='grey') #South
canvas.create_rectangle(750, 300, 1300, 460, fill='grey') #East
west = Label(text="W",font=("Arial", 20, "bold"))
west.place(x=40,y=365)
east = Label(text="E",font=("Arial", 20, "bold"))
east.place(x=1260,y=365)
north = Label(text="N",font=("Arial", 20, "bold"))
north.place(x=640,y=40)
south = Label(text="S",font=("Arial", 20, "bold"))
south.place(x=640,y=700)

def line_continuous():
	global westQueueLength,northQueueLength,eastQueueLength,southQueueLength;
	canvas.create_rectangle(0, 300, 550, 460, fill='gray64') #West
	canvas.create_line(550, 380, 550-westQueueLength, 380, width=50, fill='blue')
	west1 = Label(text=""+str(westQueueLength).zfill(2))
	west1.place(x=100,y=380)
	canvas.create_rectangle(550, 0, 750, 300, fill='gray64') #North
	canvas.create_line(650, 300, 650, 300-northQueueLength, width=50, fill='orange')
	north1 = Label(text=""+str(northQueueLength).zfill(2))
	north1.place(x=645,y=100)
	canvas.create_rectangle(750, 300, 1300, 460, fill='gray64') #East
	canvas.create_line(750, 380, 750+eastQueueLength, 380, width=50, fill='navy')
	east1 = Label(text=""+str(eastQueueLength).zfill(2))
	east1.place(x=1200,y=380)
	canvas.create_rectangle(550, 460, 750, 800, fill='gray64') #South
	canvas.create_line(650, 460, 650, 460+southQueueLength, width=50, fill='brown')
	south1 = Label(text=""+str(southQueueLength).zfill(2))
	south1.place(x=645,y=650)
	Timer(0.5,line_continuous).start()

#Begin Simulation Process

#Create 3 different Timer objects for handling 3 different timeouts.
Timer(trafficTimeout,changeDirection).start()
Timer(arrival_east,arrival_east_fn).start()
Timer(arrival_west,arrival_west_fn).start()
Timer(arrival_north,arrival_north_fn).start()
Timer(arrival_south,arrival_south_fn).start()
Timer(removeTimeout,removeFromQueue).start()
printTimer=Timer(1,printInformation).start()
Timer(0.5,line_continuous).start()
mainloop()
