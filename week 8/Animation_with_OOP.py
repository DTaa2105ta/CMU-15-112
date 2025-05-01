from cmu_112_graphics import *
import random

class Dot:
    def __init__(self, cx, cy, r, counter, color):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.counter = counter
        self.color = color

    def redraw(self, app, canvas):
        # Only redraw this dot
        canvas.create_oval(self.cx-self.r, self.cy-self.r,
                           self.cx+self.r, self.cy+self.r,
                           fill='white', outline=self.color, width=15)
        canvas.create_text(self.cx, self.cy, text=str(self.counter),
                           fill='black')

    def containsPoint(self, x, y):
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r)

    def mousePressed(self, event):
        # We are guaranteed (event.x, event.y) is in this dot
        self.counter += 1
        self.color = getRandomColor()

    def timerFired(self, app):
        self.counter += 1

def appStarted(app):
    app.dots = [ ]
    app.timerDelay = 1000 # once per second

def getRandomColor():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink',
              'lightGreen', 'gold', 'magenta', 'maroon', 'salmon',
              'cyan', 'brown', 'orchid', 'purple']
    return random.choice(colors)

def mousePressed(app, event):
    # go through dots in reverse order so that
    # we find the topmost dot that intersects
    for dot in reversed(app.dots):
        if dot.containsPoint(event.x, event.y):
            dot.mousePressed(event)
            return
    # mouse click was not in any dot, so create a new dot
    newDot = Dot(cx=event.x, cy=event.y, r=20, counter=0, color='cyan')
    app.dots.append(newDot)

def keyPressed(app, event):
    if (event.key == 'd'):
        if (len(app.dots) > 0):
            app.dots.pop(0)
        else:
            print('No more dots to delete!')

def timerFired(app):
    for dot in app.dots:
        dot.timerFired(app)

def redrawAll(app, canvas):
    for dot in app.dots:
        dot.redraw(app, canvas)

    # draw the text
    canvas.create_text(app.width/2, 20,
                       text='Example: Adding and Deleting Shapes',
                       fill='black')
    canvas.create_text(app.width/2, 40,
                       text='Mouse clicks outside dots create new dots',
                       fill='black')
    canvas.create_text(app.width/2, 60,
                       text='Mouse clicks inside dots increase their counter',
                       fill='black')
    canvas.create_text(app.width/2, 70,
                       text='and randomize their color.', fill='black')
    canvas.create_text(app.width/2, 90,
                       text='Pressing "d" deletes circles', fill='black')

runApp(width=400, height=400)