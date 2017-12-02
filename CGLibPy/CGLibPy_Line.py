from .CGLibPy_Point import CGLibPy_Point
from .CGLibPy_Vector import CGLibPy_Vector
from .CGLibPy_Utility import *

class CGLibPy_Line(object):
    startPt = None
    endPt = None
    midpt = None
    vec = None
    lineLen = 0.0

    def createMidPt(self):
        self.midpt = CGLibPy_Point((self.startPt.X + self.endPt.X)/2,
                                   (self.startPt.Y + self.endPt.Y)/2,
                                   (self.startPt.Z + self.endPt.Z)/2)

    def createVector(self):
        self.vec = CGLibPy_Vector([self.startPt,self.endPt])

    def calcLength(self):
        self.lineLen = dist2Pts(self.startPt,self.endPt)

    def pointOnLine(self,param):
        x = self.startPt.X + (self.endPt.X - self.startPt.X)*param
        y = self.startPt.Y + (self.endPt.Y - self.startPt.Y)*param
        z = self.startPt.Z + (self.endPt.Z - self.startPt.Z)*param

        return (CGLibPy_Point(x,y,z))

    def __init__(self,_args):
        if len(_args) == 2:
            self.startPt = _args[0]
            self.endPt = _args[1]
        elif len(_args) == 6:
            self.startPt = CGLibPy_Point(_args[0],_args[1],_args[2])
            self.endPt = CGLibPy_Point(_args[3],_args[4],_args[5])
        
        self.createMidPt()
        self.createVector()
        self.calcLength()
        

