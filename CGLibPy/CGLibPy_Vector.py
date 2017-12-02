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

    def normalize():
        self.vecLen = dist2Pts(_args[0],_args[1])
        self.I = self.I/self.vecLen
        self.J = self.J/self.vecLen
        self.K = self.K/self.vecLen