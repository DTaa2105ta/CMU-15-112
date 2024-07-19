from cmu_112_graphics import *

def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'

def redrawAll(app, canvas):
    pistachio = rgbString(147, 197, 114)
    maroon = rgbString(176, 48, 96)
    canvas.create_rectangle(0, 0, app.width/2, app.height/2,
                            fill=pistachio, outline='black')
    canvas.create_rectangle(app.width/2, app.height/2, app.width, app.height,
                            fill=maroon, outline='black')

runApp(width=400, height=200)