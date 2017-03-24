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
            fixed=random.randint(0,10)
        elif type=="car":
            fixed=random.randint(1,9)
        elif type=="truck":
            fixed=random.randint(2,8)

    if direction=="southLeft" or direction=="eastDown":
        if type=="bike":
            fixed=random.randint(-11,-1)
        elif type=="car":
            fixed=random.randint(-10,0)
        elif type=="truck":
            fixed=random.randint(-9,1)

    typeOfDriver=["aggressive","non aggressive","semi aggressive"][random.randint(0,2)]
    newVehicle=Vehicle(id,fixed,typeOfDriver,type,direction)
    addVehicleToEnvironment(id,newVehicle)
    return newVehicle

vehicle=createVehicle()

vehicle.start()
