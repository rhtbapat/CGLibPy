class CGLibPy_Vector(object):
    I = 0.0
    J = 0.0
    K = 0.0

    def __init__(self,_args):
        if _args.length() == 3:
            self.I = _args[0]
            self.J = _args[1]
            self.K = _args[2]
        elif _args.length() == 2:
            self.I = _args[1].X - _args[0].X
            self.J = _args[1].Y - _args[0].Y
            self.K = _args[1].Z - _args[0].Z