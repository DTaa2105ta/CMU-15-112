from cmu_112_graphics import *

def redrawAll(app, canvas):
    # Dynamically sizing text is harder, but possible!
    # Just compute the font size based on the width or height
    # Some guesswork helps to get the ratio right
    textSize = app.width // 10
    canvas.create_text(app.width/2, app.height/2, text='Hello, World!',
                        font=f'Arial {textSize} bold', fill='black')

runApp(width=400, height=400)
