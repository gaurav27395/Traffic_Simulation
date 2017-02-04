from Tkinter import *
from threading import Timer
canvas = Canvas(width=500, height=500, bg='grey')  
canvas.pack(expand=YES, fill=BOTH)                

canvas.create_oval(200, 200, 300, 300, fill='black')
canvas.create_rectangle(200, 0, 300, 200, fill='black')
canvas.create_rectangle(0, 200, 200, 300, fill='black')
canvas.create_rectangle(300, 200, 500, 300, fill='black')
canvas.create_rectangle(200, 300, 300, 500, fill='black')
u=0
x=250
y=200
z=250
def line_continuous():
	global x,y,u
	canvas.create_rectangle(0, 200, 200, 300, fill='black')

	canvas.create_line(u, x, y, z, dash=(3,5),fill='white')
	
	u=u+10
	y=y-10
	
	Timer(0.05,line_continuous).start()



Timer(0.5,line_continuous).start()
mainloop()
