#Controls the operation of a vehicle

from Microscopic.Driver import *
from Microscopic.Environment import *
from Microscopic.Behaviour import *
from Microscopic.Vehicle import *
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
            fixed=random.randint(0,9)
        elif type=="car":
            fixed=random.randint(0,8)
        elif type=="truck":
            fixed=random.randint(0,6)

    if direction=="southLeft" or direction=="eastDown":
        if type=="bike":
            fixed=random.randint(-9,0)
        elif type=="car":
            fixed=random.randint(-8,0)
        elif type=="truck":
            fixed=random.randint(-6,0)

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
    addVehicleToGUI(vehicle)

def addVehicleToGUI(vehicle):
    xposition = vehicle.position[0] * 1.625 + 400
    yposition = vehicle.position[0] * 0.975 + 400

    if vehicle.type == 'car':
        canvas.create_rectangle(xposition, yposition,xposition+10, yposition+5, outline='blue', fill='blue')
    elif vehicle.type == 'bus':
        canvas.create_rectangle(xposition, yposition,xposition+20, yposition+10, outline='blue', fill='blue')
    elif vehicle.type == 'bike':
        canvas.create_rectangle(xposition, yposition,xposition+8, yposition+3, outline='blue', fill='blue')



#The following line of code are used for creating the input GUI
window=tkinter.Tk()
window.geometry("1300x800")


canvas = tkinter.Canvas(window,width=1300, height=800, bg='gray11')
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

simulationLabel=tkinter.Label(canvas,text="Traffic Simulation",font=("Helvetica", 20))
simulationLabel.place(x=20,y=20)

directionVariable=tkinter.StringVar(window)
directionVariable.set("Random")
directionMenu = tkinter.OptionMenu(window,directionVariable,"Random","northRight", "southLeft", "eastDown","westUp")
directionMenu.place(x=20,y=60)

typeVariable=tkinter.StringVar(window)
typeVariable.set("Random")
typeMenu=tkinter.OptionMenu(window,typeVariable,"Random","car","bus","bike")
typeMenu.place(x=120,y=60)

button=tkinter.Button(window,text="ADD VEHICLE",bg="white",command=lambda: introduceNewVehicle(directionVariable.get(),typeVariable.get()))
button.place(x=250,y=60)

window.mainloop()
