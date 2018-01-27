import math

class CGLibPy_Point(object):
    X = 0.0
    Y = 0.0
    Z = 0.0
    connectedCurves = []

    def __init__(self, xcoord,ycoord,zcoord):
        self.X = xcoord
        self.Y = ycoord
        self.Z = zcoord

    def addConnectedCurve(self, curve):
        if len(self.connectedCurves) == 0 or curve in self.connectedCurves:
            self.connectedCurves.append(curve)

    def samePoint(self,point):
        if (math.isclose(self.X,point.X) and math.isclose(self.Y,point.Y) and math.isclose(self.Z,point.Z)):
            return True 
        else:
            return False

    def translateBy(self,transVec = [0,0,0]):
        self.X += transVec[0]
        self.Y += transVec[1]
        self.Z += transVec[2]
    
    def translateAlongVec(self,dist=0,vec=[1,0,0]):
        if(math.isclose(math.sqrt(vec[0]**2+vec[1]**2+vec[2]**2)),1):
            self.X += dist*vec[0]
            self.Y += dist*vec[1]
            self.Z += dist*vec[2]

    def rotate(self,ang=0,pt=[0,0,0],vec=[0,0,1]):
        if(math.isclose(math.sqrt(vec[0]**2+vec[1]**2+vec[2]**2)),1 == False):
            return

        cang = math.cos(ang)
        CAng = 1-cang
        SAng = math.sin(ang)
        row1 = [cang+vec[0]*vec[0]*CAng,
                vec[0]*vec[1]*CAng-vec[2]*SAng,
                vec[0]*vec[2]*CAng+vec[1]*SAng]

        row2 = [vec[1]*vec[0]*CAng+vec[2]*SAng,
                cang+vec[1]*vec[1]*CAng,
                vec[1]*vec[2]*CAng-vec[0]*SAng]

        row3 = [vec[2]*vec[0]*CAng-vec[1]*SAng,
                vec[2]*vec[1]*CAng+vec[0]*SAng,
                cang+vec[2]*vec[2]*CAng]

        
        self.translateBy(-pt[0],-pt[1],-pt[2])

        self.X = self.X*row1[0] + self.Y*row1[1] + self.Z*row1[2]
        self.Y = self.X*row2[0] + self.Y*row2[1] + self.Z*row2[2]
        self.Z = self.X*row3[0] + self.Y*row3[1] + self.Z*row3[2]

        self.translateBy(pt[0],pt[1],pt[2])

    def scale(self,x=1,y=1,z=1):
        self.X *= x
        self.Y *= y
        self.Z *= z

    def shear(self,xShear=[1,1],yShear=[1,1],zShear=[1,1]):
        self.X += xShear[0]*self.Y + xShear[1]*self.Z
        self.Y += yShear[0]*self.X + yShear[1]*self.Z
        self.Z += zShear[0]*self.X + zShear[1]*self.Y

    def transformBy(self,transF):
        if transF.transType == 0:
            if transF.transByXYZ:
                self.translateBy(transF.translateXYZ)
            else:
                self.translateAlongVec(transF.transDist,transF.transVecs)
        elif transF.transType == 1:
            self.rotate(transF.rotAng,transF.rotPt,transF.rotVec);
        elif transF.transType == 2:
            self.scale(transF.scaleVec[0],transF.scaleVec[1],transF.scaleVec[2])
        elif transF.transType == 3:
            self.shear(transF.xShear,transF.yShear,transF.zShear)
            
    