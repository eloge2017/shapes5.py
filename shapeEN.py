from graphics import *

shapesWin = GraphWin ("shapes", 500, 500)
shapesWin.setCoords ( 0,0,500,500)

rTri = Polygon (Point (10, 10), Point (60,110), Point (110, 10))
rTri.setFill (color_rgb(225,0,0))
rTri.draw(shapesWin)

gOval = Oval (Point (490, 490), Point(450,375))
gOval.setFill (color_rgb(0,225,0))
gOval.draw(shapesWin)

bCir = Circle (Point(75,440), 50)
bCir.setFill(color_rgb(0,0,225))
bCir.draw(shapesWin)

shapesWin.getMouse ()
shapesWin.close()

