#Controls the operation of a vehicle

from Driver import *
from Environment import *
from Behaviour import *
from Vehicle import *
from threading import Timer
import tkinter

totalVehicleCount=0


def createVehicle(vehicleDirection,vehicleType):
    global totalVehicleCount
    totalVehicleCount+=1
    id=totalVehicleCount+1

    if vehicleDirection=="Random":
        direction=["northRight","southLeft","eastDown","westUp"][random.randint(0,3)]
    else:
        direction=vehicleDirection

    if vehicleType=="Random":
        type = ["bike", "car", "truck"][random.randint(0, 2)]
    else:
        type=vehicleType

    fixed=0
    if direction=="northRight" or direction=="westUp":
        if type=="bike":
            fixed=random.randint(5,5)
        elif type=="car":
            fixed=random.randint(5,5)
        elif type=="truck":
            fixed=random.randint(5,5)

    if direction=="southLeft" or direction=="eastDown":
        if type=="bike":
            fixed=random.randint(-5,-5)
        elif type=="car":
            fixed=random.randint(-5,-5)
        elif type=="truck":
            fixed=random.randint(-5,-5)

    typeOfDriver=["aggressive","non aggressive","semi aggressive"][random.randint(0,2)]
    newVehicle=Vehicle(id,fixed,typeOfDriver,type,direction)
    number = random.random()

    if number < 0.33:
        newVehicle.turnLeft = True
        newVehicle.turnRight = False

    elif number < 0.66:
        newVehicle.turnLeft = False
        newVehicle.turnRight = True

    else:
        newVehicle.turnRight = False
        newVehicle.turnLeft = False

    addVehicleToEnvironment(id,newVehicle)
    print("A new vehicle was created ")
    return newVehicle

def introduceNewVehicle(direction=None,type=None):
    vehicle=createVehicle(direction,type)
    vehicle.start()
    vehicle.printVehicleInformation()

#The following line of code are used for creating the input GUI
window=tkinter.Tk()
window.geometry("300x300")

simulationLabel=tkinter.Label(window,text="Traffic Simulation",font=("Helvetica", 20))
simulationLabel.pack()

directionVariable=tkinter.StringVar(window)
directionVariable.set("Random")
directionMenu = tkinter.OptionMenu(window,directionVariable,"Random","northRight", "southLeft", "eastDown","westUp")
directionMenu.pack()


typeVariable=tkinter.StringVar(window)
typeVariable.set("Random")
typeMenu=tkinter.OptionMenu(window,typeVariable,"Random","car","bus","bike")
typeMenu.pack()

button=tkinter.Button(window,text="ADD VEHICLE",command=lambda: introduceNewVehicle(directionVariable.get(),typeVariable.get()))
button.pack()

window.mainloop()
