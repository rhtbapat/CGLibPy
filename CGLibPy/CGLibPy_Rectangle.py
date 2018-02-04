from .CGLibPy_Polygon import CGLibPy_Polygon

class CGLibPy_Rectangle(CGLibPy_Polygon):
    length = 0.0
    width = 0.0

    def __init__(self,input,inputType=1):
        # Input only points
        if inputType == 1:
            if(input != None and len(input) == 4):
                for pt in input:
                    self.points.append(pt)
            self.createLinesFromPoints();

    def translateBy(self,dx,dy,dz):
        for pt in self.points:
            pt.translateBy(dx,dy,dz)
        for ln in self.entities:
            ln.translateBy(dx,dy,dz)

    def transformBy(self,transF):
        for pt in self.points:
            pt.transformBy(transF)
        for ln in self.entities:
            ln.transformBy(transF)
