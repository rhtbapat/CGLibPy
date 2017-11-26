import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import CGLibPy

point = CGLibPy.CGLibPy_Point(10,20,30)

line = CGLibPy.CGLibPy_Line([20,10,30,40,20,12])

print(point.X)
print(line.startPt.Z)
print(line.midpt.Y)
print(line.vec.K)
print(line.lineLen)

