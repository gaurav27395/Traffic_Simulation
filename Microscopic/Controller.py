#Controls the operation of a vehicle

from Driver import *
from Environment import *
from Behaviour import *
from Vehicle import *
from threading import Timer

totalVehicleCount=0


def createVehicle():
    global totalVehicleCount
    totalVehicleCount+=1
    id=totalVehicleCount+1
    type=["bike","car","truck"][random.randint(0,2)]
    direction=["northRight","southLeft","eastDown","westUp"][random.randint(0,3)]
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
    return newVehicle

vehicle=createVehicle()
vehicle.start()
vehicle.printVehicleInformation()
vehicle1=createVehicle()
vehicle1.start()
vehicle1.printVehicleInformation()
