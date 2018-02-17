class CGLibPy_Arc(object):
    centrePt = None
    startPt = None
    endPt = None
    radius = 0.0
    startAng = 0.0
    endAng = 0.0
    sweepAng = 0.0
    fullCircle = False
    CCW = True

    def __init__(self,*args):
        if len(args) == 3: #Circle - Centre, radius, Orientation
            self.centrePt = args[0]
            self.radius = args[1]
            self.CCW = args[2]
            self.fullCircle = True
        elif len(args) == 5: #Arc - Centre, Start Pt, End Pt, radius, Orientation
            self.centrePt = args[0]
            self.startPt = args[1]
            self.endPt = args[2]
            self.radius = args[3]
            self.CCW = args[4]

    def translateBy(self,dx,dy,dz):
        if self.startPt != None and self.endPt != None:
            self.startPt.translateBy(dx,dy,dz)
            self.endPt.translateBy(dx,dy,dz)
        self.centrePt.translateBy(dx,dy,dz)

    def transformBy(self,transF):
        if self.startPt != None and self.endPt != None:
            self.startPt.transformBy(transF)
            self.endPt.transformBy(transF)
        self.centrePt.transformBy(transF)
            
