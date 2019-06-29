### Turtle grapher (example of HOFs)
### Docs: https://docs.python.org/3.7/library/turtle.html

from turtle import *
from math import sin,cos,tan,pi,sqrt

def setup(size):
	"Set up parameters for the graph, between -SIZE and SIZE"
	setworldcoordinates(-0.05,-0.05,1.05,1.05)
	speed("fastest")

def triangle(x,y,side):
	pu()
	goto(x,y)
	n = 3
	begin_fill()
	while n > 0:
		fd(side)
		lt(120)
		n -= 1
	end_fill()

### GRAPHER -- write this in real time 

def grapher(f):
	"Graph the function y=f(x)"
	goto(-1,f(-1))
	pd()
	x = -1
	step = 0.005
	while x < 1:
		goto(x,f(x))
		x += step
	pu()

setup(1.05)
#coords()
#pen(pencolor="red", pensize=10)
#grapher(abs)
#pen(pencolor="blue", pensize=10)
#grapher(lambda t: tan(t*pi))
#pen(pencolor="green", pensize=10)
#grapher(lambda t: sin(t*2*pi))
#triangle(-1,-1,2)
def sierpinski(x,y,side,n):
	if n == 0:
		triangle(x,y,side)
	else:
		sierpinski(x,y,side/2,n-1)
		sierpinski(x+side/2,y,side/2,n-1)
		sierpinski(x+side/4,y+(sqrt(3)/4)*side,side/2,n-1)

sierpinski(0,0,1,6)
