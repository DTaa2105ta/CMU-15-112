from cmu_112_graphics import *

def redrawAll(app, canvas):
    margin = 10
    # Approach #1: Add margin to top/left, subtract margin from bottom/right:
    canvas.create_rectangle(margin, margin, app.width-margin, app.height-margin,
                            fill='darkGreen', outline='black')
    # Approach #2: add/subtract app.width/app.height from center (cx, cy)
    (cx, cy) = (app.width/2, app.height/2)
    (rectWidth, rectHeight) = (app.width/4, app.height/4)
    canvas.create_rectangle(cx - rectWidth/2, cy - rectHeight/2,
                            cx + rectWidth/2, cy + rectHeight/2,
                            fill='orange', outline='black')

runApp(width=400, height=200)