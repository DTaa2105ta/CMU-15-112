from cmu_112_graphics import *

def redrawAll(app, canvas):
    # most graphics functions allow you to use optional parameters
    # to change the appearance of the object. These are written with the code
    # paramName=paramValue
    # after the core parameters in the code

    # fill changes the internal color of the shape
    canvas.create_rectangle(  0,   0, 150, 150, fill='yellow', outline='black')
    # width changes the size of the border
    canvas.create_rectangle(100,  50, 250, 100, fill='orange', 
                            outline='black', width=5)
    # outline changes the color of the border
    canvas.create_rectangle( 50, 100, 150, 200, fill='green',
                                                outline='red', width=3)
    # width=0 removes the border entirely
    canvas.create_rectangle(125,  25, 175, 190, fill='purple', width=0)

runApp(width=1200, height=600)

