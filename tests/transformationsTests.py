import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import CGLibPy

line1 = CGLibPy.CGLibPy_Line(0,0,0,1,1,1)
tr1 = CGLibPy.CGLibPy_TransF()
tr1.setTranslationXYZ(5,5,5)
line1.transformBy(tr1)
print (line1)

c1 = CGLibPy.CGLibPy_Point(1,1,1)
rad1 = 5.0
arc1 = CGLibPy.CGLibPy_Arc(c1,rad1,True)
tr2 = CGLibPy.CGLibPy_TransF()
tr2.setTranslationVec(2.5,[0.956,0.27,-0.1156]) 
arc1.transformBy(tr2)

line2 = CGLibPy.CGLibPy_Line(2.5,-3.0,-1.24,12,-19.4,-4.56)
tr3 = CGLibPy.CGLibPy_TransF()
tr3.setRotation(25,[2,2.5,-3],[-0.956,-0.27,0.1156])
line2.transformBy(tr3)
print (line2)

p1 = CGLibPy.CGLibPy_Point(10,5,20)
p2 = CGLibPy.CGLibPy_Point(20,5,20)
p3 = CGLibPy.CGLibPy_Point(20,15,20)
p4 = CGLibPy.CGLibPy_Point(10,15,20)
rect1 = CGLibPy.CGLibPy_Rectangle([p1,p2,p3,p4])
tr4 = CGLibPy.CGLibPy_TransF()
tr4.setScaling(2.5,1.25,3.4)
rect1.transformBy(tr4)
print(rect1)