import math

def distCoords(X1,Y1,Z1,X2,Y2,Z2):
    lineLen = math.sqrt((X2 - X1)*(X2 - X1)
                        +
                        (Y2 - Y1)*(Y2 - Y1)
                        +
                        (Z2 - Z1)*(Z2 - Z1))
    return lineLen


def dist2Pts(startPt,endPt):
    return distCoords(startPt.X,startPt.Y,startPt.Z,endPt.X,endPt.Y,endPt.Z)

def dotProduct3D(vector1,vector2):
    dp = vector1[0]*vector2[0] + vector1[1]*vector2[1] + vector1[2]*vector2[2] 
    return dp

def crossProduct3D(vector1,vector2):
    a = vector1[1]*vector2[2]-vector1[2]*vector2[1]
    b = vector1[2]*vector2[0]-vector1[0]*vector2[2]
    c = vector1[0]*vector2[1]-vector1[1]*vector2[0]
    cp = [a,b,c]
    return cp

def getDistance2DXY(point1,point2):
    d = sqrt(sqr(point2[0]-point1[0]) + sqr(point2[1]-point1[1]))
    return d


def getDistance2DYZ(point1,point2):
    d = sqrt(sqr(point2[1]-point1[1]) + sqr(point2[2]-point1[2]))
    return d


def getDistance2DXZ(point1,point2):
    d = sqrt(sqr(point2[0]-point1[0]) + sqr(point2[2]-point1[2]))
    return d

def lineLineIntersection3DPointsParameters(p1,p2,p3,p4):
    p13X = p1.X - p3.X;
    p13Y = p1.Y - p3.Y;
    p13Z = p1.Z - p3.Z;
    p43X = p4.X - p3.X;
    p43Y = p4.Y - p3.Y;
    p43Z = p4.Z - p3.Z;

    if (math.isclose(math.fabs(p43X),0.0) 
        and math.isclose(math.fabs(p43Y),0.0) 
        and math.isclose(math.fabs(p43Z),0.0)) :
        return false,-1,-1 #bool,u,v

    p21X = p2.X - p1.X;
    p21Y = p2.Y - p1.Y;
    p21Z = p2.Z - p1.Z;

    if (math.isclose(math.fabs(p21X),0.0) 
        and math.isclose(math.fabs(p21Y),0.0) 
        and math.isclose(math.fabs(p21Z),0.0)) :
        return False,-1,-1 #bool,u,v

    d1343 = p13X * p43X + p13Y * p43Y + p13Z * p43Z;
    d4321 = p43X * p21X + p43Y * p21Y + p43Z * p21Z;
    d1321 = p13X * p21X + p13Y * p21Y + p13Z * p21Z;
    d4343 = p43X * p43X + p43Y * p43Y + p43Z * p43Z;
    d2121 = p21X * p21X + p21Y * p21Y + p21Z * p21Z;

    denom = d2121 * d4343 - d4321 * d4321;

    if(math.isclose(math.fabs(denom),0.0)):
        return False,-1,-1 #bool,u,v

    numer = d1343 * d4321 - d1321 * d4343;

    u = numer / denom;
    v = (d1343 + d4321 * (u)) / d4343;

    return True,u,v


def lineLineIntersection3D(line1,line2):
    intersect,u,v = lineLineIntersection3DPointsParameters(line1.startPt,line1.endPt,line2.startPt,line2.endPt)

    if(intersect == True):
        p1 = line1.pointOnLine(u)
        p2 = line2.pointOnLine(v)

        d = dist2Pts(p1,p2)

        if (math.isclose(d,0.0)):
            intersect = True
        else:
            intersect = False

    return intersect,u,v
        
    
    

