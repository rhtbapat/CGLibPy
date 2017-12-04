from .CGLibPy_Line import CGLibPy_Line

class CGLibPy_Polygon(object):
    points = []
    entities = []

    def __init__(self,input,inputType):
        # Input only points
        if inputType == 1:
            if(input != None):
                for pt in input:
                    self.points.append(pt)
            self.createLinesFromPoints()
        
        # Input Lines and Arcs
        if inputType == 2:
            if(input != None):
                for entity in input:
                    self.entities.append(entity)

    def createLinesFromPoints(self):
        for i in range (0,len(self.points)-1):
            pt1 = self.points[i]
            pt2 = self.points[i+1]
            self.entities.append(CGLibPy_Line([pt1,pt2]))
        pt1 = self.points[len(self.points)-1]
        pt2 = self.points[0]
        self.entities.append(CGLibPy_Line([pt1,pt2]))
            
    
