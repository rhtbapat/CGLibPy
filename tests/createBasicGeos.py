import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import CGLibPy

point = CGLibPy.CGLibPy_Point(10,20,30)

line = CGLibPy.CGLibPy_Line([0,0,0,10,0,0])
line2 = CGLibPy.CGLibPy_Line([10,10,0,10,10,20])
line3 = CGLibPy.CGLibPy_Line([0,0,0,0,10,0])
line4 = CGLibPy.CGLibPy_Line([10,0,0,10,10,0])

print(point.X)
print(line.startPt.Z)
print(line.midpt.Y)
print(line.vec.K)
print(line.lineLen)
print(CGLibPy.CGLibPy_Utility.lineLineIntersection3D(line,line2))
print(CGLibPy.CGLibPy_Utility.ang2LinesDegrees(line,line2))
print(CGLibPy.CGLibPy_Utility.areLinesPerpendicular(line,line3))
print(CGLibPy.CGLibPy_Utility.areLinesParallel(line,line3))
intPt = line.intersectionPoint(line4)
print(intPt.X)

