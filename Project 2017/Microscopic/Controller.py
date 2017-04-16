#Controls the operation of a vehicle

from Microscopic.Driver import *
from Microscopic.Environment import *
from Microscopic.Behaviour import *
from Microscopic.Vehicle import *
from threading import Timer
import tkinter
import time




def createVehicle(vehicleDirection,vehicleType):
    global totalVehicleCount
    totalVehicleCount+=1
    id=totalVehicleCount+1

    if vehicleDirection=="Random":
        direction=["northRight","southLeft","eastDown","westUp"][random.randint(0,3)]
    else:
        direction=vehicleDirection

    if vehicleType=="Random":
        type = ["bike", "car", "bus"][random.randint(0, 2)]
    else:
        type=vehicleType

    fixed=0
    if direction=="northRight":
        if type=="bike":
            fixed=random.randint(660,740)
        elif type=="car":
            fixed=random.randint(670,730)
        elif type=="bus":
            fixed=random.randint(680,720)

        if "northRight" not in countOfVehicles:
            countOfVehicles["northRight"]=1
        else:
            countOfVehicles["northRight"]+=1

            totalCount["northRight"]+=1

            if  TrafficLight.strategyToUse=="Count" or TrafficLight.strategyToUse=="Time":
                permanentCount["northRight"]+=1
            else:
                smartPermanentCount["northRight"]+=1

    if  direction=="westUp":
        if type=="bike":
            fixed=random.randint(310,360)
        elif type=="car":
            fixed=random.randint(320,360)
        elif type=="bus":
            fixed=random.randint(330,350)

        if "westUp" not in countOfVehicles:
            countOfVehicles["westUp"]=1
        else:
            countOfVehicles["westUp"]+=1

            totalCount["westUp"] += 1
            if TrafficLight.strategyToUse=="Count" or TrafficLight.strategyToUse=="Time":
                permanentCount["westUp"]+=1
            else:
                smartPermanentCount["westUp"]+=1

    if direction=="southLeft":
        if type=="bike":
            fixed=random.randint(560,640)
        elif type=="car":
            fixed=random.randint(570,630)
        elif type=="bus":
            fixed=random.randint(580,620)
            
        if "southLeft" not in countOfVehicles:
            countOfVehicles["southLeft"]=1
        else:
            countOfVehicles["southLeft"]+=1

            totalCount["southLeft"] += 1
            if TrafficLight.strategyToUse=="Count" or TrafficLight.strategyToUse=="Time":
                permanentCount["southLeft"]+=1
            else:
                smartPermanentCount["southLeft"]+=1

    if direction=="eastDown":
        if type=="bike":
            fixed=random.randint(390,450)
        elif type=="car":
            fixed=random.randint(400,440)
        elif type=="bus":
            fixed=random.randint(410,430)
        
        if "eastDown" not in countOfVehicles:
            countOfVehicles["eastDown"]=1
        else:
            countOfVehicles["eastDown"]+=1

            totalCount["eastDown"] += 1

            if TrafficLight.strategyToUse=="Count" or TrafficLight.strategyToUse=="Time":
                permanentCount["eastDown"]+=1
            else:
                smartPermanentCount["eastDown"]+=1

    typeOfDriver=["aggressive","non aggressive","semi aggressive"][random.randint(0,2)]
    newVehicle=Vehicle(id,fixed,typeOfDriver,type,direction)
    number = random.random()

    if number < 0.33:
        newVehicle.turnLeft = False
        newVehicle.turnRight = True

    elif number < 0.66:
        newVehicle.turnLeft = True
        newVehicle.turnRight = False

    else:
        newVehicle.turnRight = False
        newVehicle.turnLeft = False

    addVehicleToEnvironment(id,newVehicle)
    return newVehicle


def introduceNewVehicle(direction=None,type=None):
    vehicle=createVehicle(direction,type)
    addVehicleToGUI(vehicle)
    vehicle.start()
    #vehicle.printVehicleInformation()


def addVehicleToGUI(vehicle):
    xposition = vehicle.position[0]
    yposition = vehicle.position[1]
    temp=vehicle.position
    lastPositionDictionary[vehicle.id] = temp

    if vehicle.type == 'car':
        vehicle.guiRectangle=canvas.create_rectangle(xposition, yposition,xposition+10, yposition+5, outline='blue', fill='blue')

    elif vehicle.type == 'bus':
        vehicle.guiRectangle=canvas.create_rectangle(xposition, yposition,xposition+20, yposition+10, outline='blue', fill='blue')

    elif vehicle.type == 'bike':
        vehicle.guiRectangle =canvas.create_rectangle(xposition, yposition,xposition+8, yposition+3, outline='blue', fill='blue')

    moveVehicle(vehicle)

def moveVehicle(vehicle):
    Timer(0.1,moveVehicleHelper,(vehicle,)).start()

def moveVehicleHelper(vehicle):
    newPosition=vehicle.position
    lastPosition=lastPositionDictionary[vehicle.id]
    lastPositionDictionary[vehicle.id]=newPosition


    if vehicle.direction=="northRight" or vehicle.direction=="southLeft":
        canvas.move(vehicle.guiRectangle,  0,newPosition[1] - canvas.coords(vehicle.guiRectangle)[1])
    else:
        canvas.move(vehicle.guiRectangle, newPosition[0]-canvas.coords(vehicle.guiRectangle)[0], 0)

    vehicle.guiTimer=Timer(0.05,moveVehicleHelper,(vehicle,))
    vehicle.guiTimer.start()

#The following line of code are used for creating the input GUI
window=tkinter.Tk()
window.geometry("1300x800")


canvas = tkinter.Canvas(window,width=1300, height=800, bg='gray11')
sendCanvasReference(canvas)
canvas.pack()
canvas.create_rectangle(550, 300, 750, 460, fill='gray26')
canvas.create_rectangle(0, 0, 550, 300, fill='navajo white')
canvas.create_rectangle(0, 460, 550, 800, fill='navajo white')
canvas.create_rectangle(750, 460, 1300, 800, fill='navajo white')
canvas.create_rectangle(750, 0, 1300, 300, fill='navajo white')
canvas.create_rectangle(550, 0, 750, 300, fill='grey') #North
canvas.create_rectangle(0, 300, 550, 460, fill='grey') #West
canvas.create_rectangle(550, 460, 750, 800, fill='grey') #South
canvas.create_rectangle(750, 300, 1300, 460, fill='grey') #East

canvas.create_line(650, 0, 650, 300, fill="white", dash=(30, 20), width= 7)
canvas.create_line(650, 460, 650, 780, fill="white", dash=(30, 20), width= 7)
canvas.create_line(0, 375, 550, 375, fill="white", dash=(30, 20), width= 7)
canvas.create_line(770, 375, 1300, 375, fill="white", dash=(30, 20), width= 7)

simulationLabel=tkinter.Label(canvas,text="Traffic Simulation",font=("Helvetica", 20))
simulationLabel.place(x=20,y=20)

allowedDirectionLabel=tkinter.Label(canvas,text="Allowed Direction: "+getAllowedDirection(),font=("Helvetica", 20))
allowedDirectionLabel.place(x=900,y=20)

directionVariable=tkinter.StringVar(window)
directionVariable.set("Random")
directionMenu = tkinter.OptionMenu(window,directionVariable,"Random","northRight", "southLeft", "eastDown","westUp")
directionMenu.place(x=20,y=60)

typeVariable=tkinter.StringVar(window)
typeVariable.set("Random")
typeMenu=tkinter.OptionMenu(window,typeVariable,"Random","car","bus","bike")
typeMenu.place(x=120,y=60)

statisticsLabel = tkinter.Label(canvas, text="Statistics:", font=("Helvetica", 16))
statisticsLabel.place(x=760, y=470)

directionLabel = tkinter.Label(canvas, text="|Direction|", font=("Helvetica", 10))
directionLabel.place(x=760, y=500)

numberOfVehiclesLabel = tkinter.Label(canvas, text="|Vehicles|", font=("Helvetica", 10))
numberOfVehiclesLabel.place(x=860, y=500)

waitingTimeLabel = tkinter.Label(canvas, text="|Normal Waiting Time|", font=("Helvetica", 10))
waitingTimeLabel.place(x=980, y=500)

waitingTimeLabel = tkinter.Label(canvas, text="|Smart Waiting Time|", font=("Helvetica", 10))
waitingTimeLabel.place(x=1150, y=500)

southLeftLabel = tkinter.Label(canvas, text="south", font=("Helvetica", 10))
northRightLabel = tkinter.Label(canvas, text="north", font=("Helvetica", 10))
eastDownLabel = tkinter.Label(canvas, text="east", font=("Helvetica", 10))
westUpLabel = tkinter.Label(canvas, text="west", font=("Helvetica", 10))

southLeftLabel.place(x=760, y=540)
northRightLabel.place(x=760, y=580)
eastDownLabel.place(x=760, y=620)
westUpLabel.place(x=760, y=660)

strategyVariable=tkinter.StringVar(window)
strategyVariable.set("Normal")
strategyMenu=tkinter.OptionMenu(window,strategyVariable,"Normal","Count","Time")
strategyMenu.place(x=900,y=60)

def changeSmartTrafficStatus(strategy):
    TrafficLight.strategyToUse=strategy

smartTrafficButton=tkinter.Button(window,text="MAKE IT SMART",font=("Arial", 15),command=lambda: changeSmartTrafficStatus(strategyVariable.get()))
smartTrafficButton.place(x=1000,y=60)


def calculateAverageTime():
    for id in vehicleStatusMap:
        vehicle=vehicleStatusMap[id]
        if(vehicle.doNotStop and not vehicle.waitingTimeAdded):
            vehicle.waitingTimeAdded=True
            diffTime=vehicle.exitTime-vehicle.entryTime

            if TrafficLight.strategyToUse=="Count" or TrafficLight.strategyToUse=="Time":
                if(vehicle.direction=='northRight'):
                    smartTiming["northRight"] +=diffTime
                if (vehicle.direction == 'southLeft'):
                    smartTiming["southLeft"] += diffTime
                if (vehicle.direction == 'eastDown'):
                    smartTiming["eastDown"] += diffTime
                if (vehicle.direction == 'westUp'):
                    smartTiming["westUp"] += diffTime
            else:
                if (vehicle.direction == 'northRight'):
                    Timing["northRight"] += diffTime
                if (vehicle.direction == 'southLeft'):
                    Timing["southLeft"] += diffTime
                if (vehicle.direction == 'eastDown'):
                    Timing["eastDown"] += diffTime
                if (vehicle.direction == 'westUp'):
                    Timing["westUp"] += diffTime
    Timer(0.1,calculateAverageTime).start()

def displayStatistics():
    allowedDirectionLabel = tkinter.Label(canvas, text="Allowed Direction: "+getAllowedDirection()+"      ", font=("Helvetica", 20))
    allowedDirectionLabel.place(x=880,y=20)

    vehiclesSouthLeftLabel = tkinter.Label(canvas, text=countOfVehicles["southLeft"], font=("Helvetica", 10))
    vehiclesNorthRightLabel = tkinter.Label(canvas, text=countOfVehicles["northRight"], font=("Helvetica", 10))
    vehiclesEastDownLabel = tkinter.Label(canvas, text=countOfVehicles["eastDown"], font=("Helvetica", 10))
    vehiclesWestUpLabel = tkinter.Label(canvas, text=countOfVehicles["westUp"], font=("Helvetica", 10))

    vehiclesSouthLeftLabel.place(x=880, y=540)
    vehiclesNorthRightLabel.place(x=880, y=580)
    vehiclesEastDownLabel.place(x=880, y=620)
    vehiclesWestUpLabel.place(x=880, y=660)


    timingSouthLeftLabel = tkinter.Label(canvas, text=str(Timing["southLeft"]/permanentCount["southLeft"]*pow(10,6))[0:4], font=("Helvetica", 10))
    timingNorthRightLabel = tkinter.Label(canvas, text=str(Timing["northRight"]/permanentCount["northRight"]*pow(10,6))[0:4], font=("Helvetica", 10))
    timingEastDownLabel = tkinter.Label(canvas, text=str(Timing["eastDown"]/permanentCount["eastDown"]*pow(10,6))[0:4], font=("Helvetica", 10))
    timingWestUpLabel = tkinter.Label(canvas, text=str(Timing["westUp"]/permanentCount["westUp"]*pow(10,6))[0:4], font=("Helvetica", 10))

    timingSouthLeftLabel.place(x=1030, y=540)
    timingNorthRightLabel.place(x=1030, y=580)
    timingEastDownLabel.place(x=1030, y=620)
    timingWestUpLabel.place(x=1030, y=660)


    smartTimingSouthLeftLabel = tkinter.Label(canvas, text=str(smartTiming["southLeft"] / smartPermanentCount["southLeft"]*pow(10,6))[0:4],font=("Helvetica", 10))
    smartTimingNorthRightLabel = tkinter.Label(canvas, text=str(smartTiming["northRight"] / smartPermanentCount["northRight"]*pow(10,6))[0:4],font=("Helvetica", 10))
    smartTimingEastDownLabel = tkinter.Label(canvas, text=str(smartTiming["eastDown"] / smartPermanentCount["eastDown"]*pow(10,6))[0:4],font=("Helvetica", 10))
    smartTimingWestUpLabel = tkinter.Label(canvas, text=str(smartTiming["westUp"] / smartPermanentCount["westUp"]*pow(10,6))[0:4], font=("Helvetica", 10))

    smartTimingSouthLeftLabel.place(x=1180, y=540)
    smartTimingNorthRightLabel.place(x=1180, y=580)
    smartTimingEastDownLabel.place(x=1180, y=620)
    smartTimingWestUpLabel.place(x=1180, y=660)


    Timer(0.5,displayStatistics).start()

displayStatistics()
calculateAverageTime()
button=tkinter.Button(window,text="ADD VEHICLE",bg="white",command=lambda: introduceNewVehicle(directionVariable.get(),typeVariable.get()))
button.place(x=250,y=60)
window.mainloop()
