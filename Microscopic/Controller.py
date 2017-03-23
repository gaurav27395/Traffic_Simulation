#Controls the operation of a vehicle
from Microscopic.Driver import *
from Microscopic.Environment import *
from Microscopic.Behaviour import *
from Microscopic.Vehicle import *
from threading import Timer

vehicle=Vehicle("1234",3,"aggressive","bike","northRight")
vehicle1=Vehicle("1234",14,"aggressive","car","southRight")
vehicle2=Vehicle("1234",3,"aggressive","truck","east")
vehicle3=Vehicle("1234",8,"aggressive","bike","north")
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
Timer(1,a).start()
Timer(2,b).start()

