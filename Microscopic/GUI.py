import Tkinter as tk
import time
import random
from threading import Timer
from Environment import *
from Controller import *

root=tk.Tk()
root.title("Traffic Simulation")
canvas = tk.Canvas(root,width=1300, height=800, bg='gray11')
canvas.pack()

# create car

#canvas = Canvas(width=1300, height=800, bg='gray11')  
#canvas.pack(expand=YES, fill=BOTH)                
canvas.create_rectangle(550, 300, 750, 460, fill='gray26')
canvas.create_rectangle(0, 0, 550, 300, fill='navajo white')
canvas.create_rectangle(0, 460, 550, 800, fill='navajo white')
canvas.create_rectangle(750, 460, 1300, 800, fill='navajo white')
canvas.create_rectangle(750, 0, 1300, 300, fill='navajo white')
canvas.create_rectangle(550, 0, 750, 300, fill='grey') #North
canvas.create_rectangle(0, 300, 550, 460, fill='grey') #West
canvas.create_rectangle(550, 460, 750, 800, fill='grey') #South
canvas.create_rectangle(750, 300, 1300, 460, fill='grey') #East

print(vehicleStatusMap)

for id in vehicleStatusMap:
    vehicle = vehicleStatusMap[id]
    xposition = vehicle.position[0] * 3.25 +400
    yposition = vehicle.position[0] * 1.95 +400
    car1 = canvas.create_rectangle(xposition, yposition,xposition+10, yposition+5, outline='blue', fill='blue')
    for x in range(500):
        y= x = 2
        canvas.move(car1, x, 0)
        canvas.update()
    #car2 = canvas.create_rectangle(580,20,610,40, outline='blue', fill='blue')

# move car
# for x in range(500):
#     y= x = 1
#     time.sleep(0.025)
#     canvas.move(car1, x, 0)
#     #canvas.move(car2, 0, y)
#     canvas.update()

root.mainloop()