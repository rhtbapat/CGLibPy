class CGLibPy_Plane(object):
    planePoint = None
    normalVector = None

    def __init__(self,point,normalVec):
        self.planePoint = point
        self.normalVector = normalVec
    
    def translateBy(self,dx,dy,dz):
        self.planePoint.translateBy(dx,dy,dz)