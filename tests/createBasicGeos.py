import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import CGLibPy

point = CGLibPy.CGLibPy_Point(10,20,30)

line = CGLibPy.CGLibPy_Line([0,0,0,10,0,0])
line2 = CGLibPy.CGLibPy_Line([0,0,0,0,10,0])
line3 = CGLibPy.CGLibPy_Line([0,0,0,0,10,0])
line4 = CGLibPy.CGLibPy_Line([10,0,0,10,10,0])
line5 = CGLibPy.CGLibPy_Line([4.56,-12.345,34.126546,-98.5,10,54.005]) 
line6 = CGLibPy.CGLibPy_Line([0,0,0,0,10,0]) 
line7 = CGLibPy.CGLibPy_Line([0,0,0,0,0,10])

line8 = CGLibPy.CGLibPy_Line([0,0,0,10,10,10]) 
line9 = CGLibPy.CGLibPy_Line([5,5,0,12,12,12])   

arc1 = CGLibPy.CGLibPy_Arc( [CGLibPy.CGLibPy_Point(0,0,0),
                            CGLibPy.CGLibPy_Point(-5,0,0),
                            CGLibPy.CGLibPy_Point(5,0,0),
                            5, True])

point1 = CGLibPy.CGLibPy_Point(2,5,7)
point2 = CGLibPy.CGLibPy_Point(-2,5,7)
point3 = CGLibPy.CGLibPy_Point(2,5,17)
point4 = CGLibPy.CGLibPy_Point(12,-5,17)


print(point.X)
print(line.startPt.Z)
print(line.getMidPt().Y)
print(line.getVector().K)
print(line.getLength())
print(CGLibPy.CGLibPy_Utility.lineLineIntersection3D(line8,line9))
print(CGLibPy.CGLibPy_Utility.lineLineIntersection3DUsingCrossProduct(line8,line9))
print(CGLibPy.CGLibPy_Utility.ang2LinesDegrees(line,line2))
print(CGLibPy.CGLibPy_Utility.areLinesPerpendicular(line,line3))
print(CGLibPy.CGLibPy_Utility.areLinesParallel(line,line3))
intPt = line.intersectionPoint(line4)
print(intPt.X)
linePt = line5.pointAtDistAlongLine(45.342)
print(str(linePt.X) + " " + str(linePt.Y) + " " + str(linePt.Z))
print(CGLibPy.CGLibPy_Utility.SideOfThePointToLineXY(line6,point2))
print(CGLibPy.CGLibPy_Utility.SideOfThePointToLineYZ(line7,point3))
print(CGLibPy.CGLibPy_Utility.SideOfThePointToLineXZ(line7,point2))

inter,u,v = CGLibPy.CGLibPy_Utility.arcLineIntersection(line6,arc1)
print(inter)

polygon = CGLibPy.CGLibPy_Polygon([point1,point2,point3,point4],1)
polygon.entities

print(CGLibPy.CGLibPy_Utility.lineProjectOnLine(line8,line9))





