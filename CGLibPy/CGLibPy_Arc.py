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

    def __init__(self,_args):
        if len(_args) == 3: #Circle - Centre, radius, Orientation
            self.centrePt = _args[0]
            self.radius = _args[1]
            self.CCW = _args[2]
            self.fullCircle = True
        elif len(_args) == 5: #Arc - Centre, Start Pt, End Pt, radius, Orientation
            self.centrePt = _args[0]
            self.startPt = _args[1]
            self.endPt = _args[2]
            self.radius = _args[3]
            self.CCW = _args[4]

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
            
