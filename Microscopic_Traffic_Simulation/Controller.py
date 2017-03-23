#Controls the operation of a vehicle
from Driver import *
from Environment import *
from Behaviour import *
from Vehicle import *
from threading import Timer

vehicle=Vehicle("1234",3,"aggressive","bike","northRight")
vehicle1=Vehicle("1234",14,"aggressive","car","southRight")
vehicle2=Vehicle("1234",3,"aggressive","truck","eastUp")
vehicle3=Vehicle("1234",8,"aggressive","bike","westDown")
# Move already,will you?

def a():
    vehicle.pressAcceleration()
    Timer(1,a).start()
    print("first: "+str(vehicle.position))
    print("Generate All Score: " + generateAllScore(vehicle))

def b():
    vehicle1.pressAcceleration()
    Timer(1,b).start()
    print("second: "+str(vehicle1.position))
    print("Generate All Score: " + generateAllScore(vehicle1))

def c():
    vehicle2.pressAcceleration()
    Timer(1,c).start()
    print("third: "+str(vehicle2.position))
    print("Generate All Score: " + generateAllScore(vehicle2))

def d():
    vehicle3.pressAcceleration()
    Timer(1,d).start()
    print("fourth: "+str(vehicle3.position))
    print("Generate All Score: " + generateAllScore(vehicle3))
Timer(1,a).start()
Timer(1,b).start()
Timer(1,c).start()
Timer(1,d).start()

