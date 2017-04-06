from Microscopic.TrafficLight import *
from Microscopic.Environment import *

def a():
    print(getAllowedDirection())
    Timer(1,a).start()
a()
