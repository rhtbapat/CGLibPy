from .CGLibPy_Utility import *
from .CGLibPy_Point import CGLibPy_Point

class CGLibPy_Vector(object):
    I = 0.0
    J = 0.0
    K = 0.0
    vecLen = 0.0  
    vecPoint = None

    def __init__(self,*args):
        if len(args) == 3: # Three Coefficients
            self.I = args[0]
            self.J = args[1]
            self.K = args[2]
        elif len(args) == 2: # Six Coordinates
            self.I = args[1].X - args[0].X
            self.J = args[1].Y - args[0].Y
            self.K = args[1].Z - args[0].Z
        self.vecLen = math.sqrt(self.I*self.I + self.J*self.J + self.K*self.K)
        self.vecPoint = CGLibPy_Point(self.I,self.J,self.K);

    def normalize(self):        
        self.I = self.I/self.vecLen
        self.J = self.J/self.vecLen
        self.K = self.K/self.vecLen

    def unitVector(self):
        i = self.I/self.vecLen
        j = self.J/self.vecLen
        k = self.K/self.vecLen
        unitVec = CGLibPy_Vector(i,j,k)
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

    def transformBy(self,transF):
        self.vecPoint.transformBy(transF)
        self.I,self.J,self.K = self.vecPoint.X,self.vecPoint.Y,self.vecPoint.Z
            

        
