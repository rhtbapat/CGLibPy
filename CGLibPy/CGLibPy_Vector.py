from .CGLibPy_Utility import *

class CGLibPy_Vector(object):
    I = 0.0
    J = 0.0
    K = 0.0
    vecLen = 0.0  

    def __init__(self,_args):
        if len(_args) == 3:
            self.I = _args[0]
            self.J = _args[1]
            self.K = _args[2]
        elif len(_args) == 2:
            self.I = _args[1].X - _args[0].X
            self.J = _args[1].Y - _args[0].Y
            self.K = _args[1].Z - _args[0].Z
        self.vecLen = math.sqrt(self.I*self.I + self.J*self.J + self.K*self.K)

    def normalize(self):        
        self.I = self.I/self.vecLen
        self.J = self.J/self.vecLen
        self.K = self.K/self.vecLen

    def unitVector(self):
        i = self.I/self.vecLen
        j = self.J/self.vecLen
        k = self.K/self.vecLen
        unitVec = CGLibPy_Vector([i,j,k])
        return unitVec

    def isParallelVector(self,inputVec):
        ang = ang2VectorsRadian(self,inputVec)
        if math.isclose(ang,0):
            return 1 # Same Direction
        elif math.isclose(ang,pi):
            return -1 # Opposite Direction
        else:
            return 0 # Not Parallel

    def isPerpendicularVector(self,inputVec):
        dotProd = dotProduct3D(self,inputVec)
        if math.isclose(ang,0):
            return True
        else:
            return False
            

        
