from shape1 import dict
from graphics import *
import random
import time
import sys
 
if len(sys.argv) != 2:
    print ("Usage :python3", sys.argv[0], "<triangle/square/pentagon/snowflake>")
    exit()

shape = sys.argv[1]
vertices=[]
vertices=dict[shape]
print(shape)
nSides=len(vertices)
count=0
 
win=GraphWin("window",1000,600)
win.setBackground("violet")
 
if shape == "square":
    s = Rectangle(Point(250, 50.03), Point(501, 301))
    s.setOutline("black")
    s.draw(win)
if shape == "pentagon":
    s = Polygon(Point(333.76,200), Point(168,267), Point(230,401), Point(435,401), Point(500,267))
    s.setWidth(2)
    s.setOutline("black")
    s.draw(win)
 
def main(pixel):
    p=Point(pixel[0], pixel[1])
    p.draw(win)
    p.setFill("black")

def pickVertex(nSides):
    return random.randint(1, nSides) - 1
 
def midpoint(point,vertex,shape):
    if shape == "snowflake":
        return [round((point[0] + vertex[0]) / 2, 2),
                round((point[1] + vertex[1]) / 2, 2)]
    else:
        return [round((point[0] + vertex[0]) / (nSides - 1), 2),
                round((point[1] + vertex[1]) / (nSides - 1), 2)]
 
current_pos = vertices[pickVertex(nSides)]
prev_vertex = current_pos
 
if shape == "snowflake":
    for x in range(15000):
        vertex = vertices[pickVertex(nSides)]
        if prev_vertex != vertex:
            current_pos = midpoint(current_pos, vertex, shape)
            if x > 10:
                main(current_pos)
                print(current_pos)
        prev_vertex = vertex
        x += 1
else:
    for x in range(10000):
        if 6<x<15:
            time.sleep(1)
        if count==2000:
            time.sleep(1)
            count=0
        if x > 6:
            main(current_pos)
            print(current_pos)
        current_pos = midpoint(current_pos, vertices[pickVertex(nSides)],shape)
        count+=1

win.getMouse()
win.close()
