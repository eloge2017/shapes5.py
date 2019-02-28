from graphics import *

#setting window size
shapesWin = GraphWin ("shapes", 500, 500)
shapesWin.setCoords ( 0,0,500,500)

winX = 500
winY = 500

#red triangle
rTri = Polygon (Point (10, 10), Point (60,110), Point (110, 10))
rTri.setFill (color_rgb(225,0,0))
rTri.draw(shapesWin)

#green oval
gOval = Oval (Point (490, 490), Point(450,375))
gOval.setFill (color_rgb(0,225,0))
gOval.draw(shapesWin)

#blue circle
bCir = Circle (Point(75,440), 50)
bCir.setFill(color_rgb(0,0,225))
bCir.draw(shapesWin)

#purple square
pSq = Rectangle (Point(490, 10), Point(435,60))
pSq.setFill(color_rgb(255,0,255))
pSq.draw(shapesWin)

#orange diamond
oDia = Polygon (Point(winX/2-100,winY/2), Point(winX/2,winY/2+100), Point(winX/2+100,winY/2), Point(winX/2,winY/2-100))
oDia.setFill("orange")
oDia.draw(shapesWin)

#window
shapesWin.getMouse ()
shapesWin.close()

