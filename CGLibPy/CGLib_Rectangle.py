from .CGLib_Polygon import CGLibPy_Polygon

class CGLibPy_Rectangle(CGLibPy_Polygon):
    length = 0.0
    width = 0.0

    def __init__(self,input,inputType):
        # Input only points
        if inputType == 1:
            if(input != None and len(input) == 4):
                for pt in input:
                    self.points.append(pt)
            self.createLinesFromPoints();
        
        # Input Lines and Arcs
        if inputType == 2:
            if(input != None and len(input) == 4):
                for entity in input:
                    self.entities.append(entity)

    def translateBy(self,dx,dy,dz):
        for pt in self.points:
            pt.translateBy(dx,dy,dz)
        for ln in self.entities:
            ln.translateBy(dx,dy,dz)
