import Tkinter as tk
from threading import Timer

root=tk.Tk()
root.title("Traffic Simulation")
canvas = tk.Canvas(root,width=1300, height=800, bg='gray11')
canvas.pack()

car=canvas.create_rectangle(550, 300, 750, 460, fill='gray26')
lastPosition=550
newPosition=600

def a():
	global newPosition
	global lastPosition
	lastPosition=newPosition
	newPosition+=5
	Timer(1,a).start()

def b():
	canvas.move(car,newPosition-lastPosition,0)
	Timer(2,b).start()
Timer(1,a).start()
Timer(2,b).start()	

tk.mainloop()	
