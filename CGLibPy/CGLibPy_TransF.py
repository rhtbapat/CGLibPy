import math

class CGLibPy_TransF(object):
    translateXYZ = []
    transDist = 0
    transVec = [1,0,0]
    transByXYZ = True

    rotAng = 0
    rotPt = [0,0,0]
    rotVec = [0,0,1]

    scaleVec = [1,1,1]

    xShear = [1,1]
    yShear = [1,1]
    zShear = [1,1]

    transType = 0 # 0 = Translation, 1 = Rotation, 2 = Scaling, 3 = Shearing
    
    # Translation in X, Y and Z Directions
    def setTranslationXYZ(self,dx=0,dy=0,dz=0):
        self.transByXYZ = True
        self.translateXYZ = [dx,dy,dz]
        self.transType = 0

    # Translation along a vector by given distance
    def setTranslationVec(self,dist=0,vec=[1,0,0]):
        self.transByXYZ = False
        self.transDist = dist
        self.transVec = vec
        self.transType = 0
      
    # Rotation around and axis and point of rotation       
    def setRotation(self,ang=0,rotPt=[0,0,0],rotVec=[0,0,1]):
        self.rotAng = math.radians(ang);
        self.rotPt = rotPt
        self.rotVec = rotVec
        self.transType = 1

    # Scaling along X, Y and Z directions
    def setScaling(self,scaleX=1,scaleY=1,scaleZ=1):
        self.scaleVec.append(scaleX)
        self.scaleVec.append(scaleY)
        self.scaleVec.append(scaleZ)
        self.transType = 2

    # Shearing Factors along X, Y and Z Directions
    def setShear(self,xShear=[1,1],yShear=[1,1],zShear=[1,1]):
        self.xShear = xShear
        self.yShear = yShear
        self.zShear = zShear
        self.transType = 3