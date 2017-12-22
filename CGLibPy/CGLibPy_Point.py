import math

class CGLibPy_Point(object):
    X = 0.0
    Y = 0.0
    Z = 0.0
    connectedCurves = []

    def __init__(self, xcoord,ycoord,zcoord):
        self.X = xcoord
        self.Y = ycoord
        self.Z = zcoord

    def addConnectedCurve(self, curve):
        if len(self.connectedCurves) == 0 or curve in self.connectedCurves:
            self.connectedCurves.append(curve)

    def samePoint(self,point):
        if (math.isclose(self.X,point.X) and math.isclose(self.Y,point.Y) and math.isclose(self.Z,point.Z)):
            return True 
        else:
            return False