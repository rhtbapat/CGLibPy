from .CGLibPy_Point import CGLibPy_Point

class CGLibPy_Line(object):
    startPt = None
    endPt = None
    midpt = None

    def createMidPt(self):
        self.midpt = CGLibPy_Point((self.startPt.X + self.endPt.X)/2,
                                   (self.startPt.Y + self.endPt.Y)/2,
                                   (self.startPt.Z + self.endPt.Z)/2,)

    def __init__(self,_args):
        if _args.length() == 2:
            self.startPt = _args[0]
            self.endPt = _args[1]
        elif _args.length() == 6:
            self.startPt = CGLibPy_Point(_args[0],_args[1],_args[2])
            self.endPt = CGLibPy_Point(_args[3],_args[4],_args[5])
        

