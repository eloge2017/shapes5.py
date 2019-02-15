from graphics import *
rTriWin = GraphWin ("Red Triangle", 300, 300)
rTriWin.setCoords (0,0,300,300)

rTri = Polygon (Point (100, 100), Point (150,200), Point (200, 100))
rTri.setFill (color_rgb(30,30,230))
rTri.draw(rTriWin)

rTriWin.getMouse ()
rTriWin.close()
