class CGLibPy_Plane(object):
    planePoint = None
    normalVector = None

    def __init__(self,point,normalVec):
        self.planePoint = point
        self.normalVector = normalVec
    
    def translateBy(self,dx,dy,dz):
        self.planePoint.translateBy(dx,dy,dz)

    def transformBy(self,transF):
        self.planePoint.transformBy(transF)
        self.normalVector.transformBy(transF)