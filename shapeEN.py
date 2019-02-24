from graphics import *
shapesWin = GraphWin ("shapes", 500, 500)
shapesWin.setCoords ( 0,0,500,500)

rTri = Polygon (Point (25, 25), Point (75,125), Point (125, 25))
rTri.setFill (color_rgb(225,0,0))
rTri.draw(shapesWin)

gOval = Oval (Point (490, 490), Point(450,375))
gOval.setFill (color_rgb(0,225,0))
gOval.draw(shapesWin)

shapesWin.getMouse ()
shapesWin.close()

