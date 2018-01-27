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

    transType = 0 # 0 = Translation, 1 = Rotation, 2 = Scaling

    def __init__(self):
        #Nothing Added Here Yet

    def setTranslationXYZ(self,dx=0,dy=0,dz=0):
        self.transByXYZ = True
        self.translateXYZ = [dx,dy,dz]
        self.transType = 0

    def setTranslationVec(self,dist=0,vec=[1,0,0]):
        self.transByXYZ = False
        self.transDist = dist
        self.transVec = vec
        self.transType = 0
            
    def setRotation(self,ang=0,rotPt=[0,0,0],rotVec=[0,0,1]):
        self.rotAng = ang
        self.rotPt = rotPt
        self.rotVec = rotVec
        self.transType = 1

    def setScaling(self,scaleX=1,scaleY=1,scaleZ=1):
        self.scaleVec.append(scaleX);
        self.scaleVec.append(scaleY);
        self.scaleVec.append(scaleZ);
        self.transType = 2
        
        
