from cmu_112_graphics import *

def redrawAll(app, canvas):
    # create_line(x1, y1, x2, y2, fill='black')
    # draws a black line from (x1, y1) to (x2, y2)
    canvas.create_line(25, 50, app.width/2, app.height/2, fill='black')

runApp(width=400, height=200)