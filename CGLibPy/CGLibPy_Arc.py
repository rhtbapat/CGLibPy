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
        if _args.length() == 3:
            self.centrePt = _args[0]
            self.radius = _args[1]
            self.CCW = _args[2]
        elif _args.length() == 5:
            self.centrePt = _args[0]
            self.startPt = _args[1]
            self.endPt = _args[2]
            self.radius = _args[3]
            self.CCW = _args[4]
            
