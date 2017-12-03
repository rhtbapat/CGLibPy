from .CGLibPy_Point import CGLibPy_Point
from .CGLibPy_Utility import *

class CGLibPy_Polygon(object):
    points = []

    def __init__(self,pts):
        if(pts != None):
            for pt in pts:
                self.points.append(pt)
