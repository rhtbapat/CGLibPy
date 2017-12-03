from .CGLibPy_Point import CGLibPy_Point
from .CGLibPy_Vector import CGLibPy_Vector
from .CGLibPy_Utility import *

class CGLibPy_Plane(object):
    planePoint = None
    normalVector = None

    def __init__(self,point,normalVec):
        self.planePoint = point
        self.normalVector = normalVec