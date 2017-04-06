import Tkinter as tk
import time
import random
from threading import Timer
from Environment import *

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

for id in vehicleStatusMap:
    vehicle= vehicleStatusMap[id]
    car1 = canvas.create_rectangle(vehicle.position[0], vehicle.position[1],vehicle.position[0]+3, vehicle.position[1]+5, outline='blue', fill='blue')
    #car2 = canvas.create_rectangle(580,20,610,40, outline='blue', fill='blue')

# move car
for x in range(500):
    y= x = 5
    time.sleep(0.025)
    canvas.move(car1, x, 0)
    #canvas.move(car2, 0, y)
    canvas.update()

root.mainloop()