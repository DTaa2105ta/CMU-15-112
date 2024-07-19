# Circle centeres at (cx, cy) in Python graphics 
# has the set of coordinates (cx+r.cos(Theta), cy-r.cos(Theta))
# Drawing Circular Patterns with Trigonometry

from cmu_112_graphics import *

import math

def redrawAll(app, canvas):
    (cx, cy, r) = (app.width/2, app.height/2, min(app.width, app.height)/3)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='yellow', outline='black')
    r *= 0.85 # make smaller so time labels lie inside clock face
    for hour in range(12):
        hourAngle = math.pi/2 - (2*math.pi)*(hour/12)
        hourX = cx + r * math.cos(hourAngle)
        hourY = cy - r * math.sin(hourAngle)
        label = str(hour if (hour > 0) else 12)
        canvas.create_text(hourX, hourY, text=label,
                           font='Arial 16 bold', fill='black')

runApp(width=400, height=400)

