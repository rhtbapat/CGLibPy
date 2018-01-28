from .CGLibPy_Point import CGLibPy_Point
from .CGLibPy_Vector import CGLibPy_Vector
from .CGLibPy_Utility import *

class CGLibPy_Line(object):
    startPt = None
    endPt = None
        
    def __init__(self,_args):
        if len(_args) == 2: #Two Points
            self.startPt = _args[0]
            self.endPt = _args[1]
        elif len(_args) == 6: # 6 Coordinates
            self.startPt = CGLibPy_Point(_args[0],_args[1],_args[2])
            self.endPt = CGLibPy_Point(_args[3],_args[4],_args[5])
        
        if self.startPt != None and self.endPt != None:
            self.startPt.addConnectedCurve(self)
            self.endPt.addConnectedCurve(self)

    def getMidPt(self):
        midpt = CGLibPy_Point((self.startPt.X + self.endPt.X)/2,
                                (self.startPt.Y + self.endPt.Y)/2,
                                (self.startPt.Z + self.endPt.Z)/2)
        return midpt

    def getVector(self):
        vec = CGLibPy_Vector([self.startPt,self.endPt])
        return vec

    def getLength(self):
        lineLen = dist2Pts(self.startPt,self.endPt)
        return lineLen

    def pointOnLine(self,param):
        x = self.startPt.X + (self.endPt.X - self.startPt.X)*param
        y = self.startPt.Y + (self.endPt.Y - self.startPt.Y)*param
        z = self.startPt.Z + (self.endPt.Z - self.startPt.Z)*param

        return (CGLibPy_Point(x,y,z))

    def intersectionPoint(self,line):
        intPoint = None
        intersect,u,v = lineLineIntersection3D(self,line)
        if(intersect == True):
            intPoint = line.pointOnLine(v)
        return intPoint

    def pointAtDistAlongLine(self,dist):
        x,y,z = pointAtDistAlongUnitVector(self.startPt, self.getVector().unitVector(), dist)
        point = CGLibPy_Point(x,y,z)
        return point

    def translateBy(self,dx,dy,dz):
        self.startPt.translateBy(dx,dy,dz)
        self.endPt.translateBy(dx,dy,dz)
    
    def transformBy(self,transF):
        self.startPt.transformBy(transF)
        self.endPt.transformBy(transF)
        

