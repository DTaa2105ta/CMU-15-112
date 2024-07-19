from cmu_112_graphics import *

import math

def drawClock(canvas, x0, y0, x1, y1, hour, minute):
    # draw a clock in the area bounded by (x0,y0) in
    # the top-left and (x1,y1) in the bottom-right
    # with the given time
    # draw an outline rectangle
    canvas.create_rectangle(x0, y0, x1, y1, outline='black', width=1)

    # find relevant values for positioning clock
    width = (x1 - x0)
    height = (y1 - y0)
    r = min(width, height)/2
    cx = (x0 + x1)/2
    cy = (y0 + y1)/2

    # draw the clock face
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline='black', width=2)

    # adjust the hour to take the minutes into account
    hour += minute/60.0

    # find the hourAngle and draw the hour hand
    # but we must adjust because 0 is vertical and
    # it proceeds clockwise, not counter-clockwise!
    hourAngle = math.pi/2 - 2*math.pi*hour/12
    hourRadius = r*1/2
    hourX = cx + hourRadius * math.cos(hourAngle)
    hourY = cy - hourRadius * math.sin(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY, fill='black', width=1)

    # repeat with the minuteAngle for the minuteHand
    minuteAngle = math.pi/2 - 2*math.pi*minute/60
    minuteRadius = r*9/10
    minuteX = cx + minuteRadius * math.cos(minuteAngle)
    minuteY = cy - minuteRadius * math.sin(minuteAngle)
    canvas.create_line(cx, cy, minuteX, minuteY, fill='black', width=1)

def redrawAll(app, canvas):
    # Draw a large clock showing 2:30
    drawClock(canvas, 25, 25, 175, 150, 2, 30)

    # And draw a smaller one below it showing 7:45
    drawClock(canvas, 75, 160, 125, 200, 7, 45)

    # Now let's have some fun and draw a whole grid of clocks!
    width = 40
    height = 40
    margin = 5
    hour = 0
    for row in range(3):
        for col in range(4):
            left = 200 + col * width + margin
            top = 50 + row * height + margin
            right = left + width - margin
            bottom = top + height - margin
            hour += 1
            drawClock(canvas, left, top, right, bottom, hour, 0)

runApp(width=400, height=400)