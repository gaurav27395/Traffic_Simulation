#Controls the operation of a vehicle

from Driver import *
from Environment import *
from Behaviour import *
from Vehicle import *
from threading import Timer

vehicle=Vehicle("1234",3,"aggressive","bike","southLeft")
vehicle1=Vehicle("1234",14,"aggressive","car","northRight")
vehicle2=Vehicle("1234",3,"aggressive","truck","eastDown")
vehicle3=Vehicle("1234",8,"aggressive","bike","westUp")


def a():
    vehicle.pressAcceleration()
    Timer(1,a).start()
    print("first: "+str(vehicle.position))
    print("Generate All Score 1 : " + generateAllScore(vehicle)+" \n")

def b():
    vehicle1.pressAcceleration()
    Timer(1,b).start()
    print("second: "+str(vehicle1.position))
    print("Generate All Score 2 : " + generateAllScore(vehicle1)+" \n")

def c():
    vehicle2.pressAcceleration()
    Timer(1,c).start()
    print("third: "+str(vehicle2.position))
    print("Generate All Score 3 : " + generateAllScore(vehicle2)+" \n")

def d():
    vehicle3.pressAcceleration()
    Timer(1,d).start()
    print("fourth: "+str(vehicle3.position))
    print("Generate All Score 4 : " + generateAllScore(vehicle3)+" \n")

Timer(1,a).start()
Timer(2,b).start()
Timer(1,c).start()
Timer(2,d).start()

