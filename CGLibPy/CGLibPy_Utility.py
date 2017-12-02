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
    dp = vector1.I*vector2.I + vector1.J*vector2.J + vector1.K*vector2.K 
    return dp

def vectorLength(vec):
    return math.sqrt(vec.I*vec.I + vec.J*vec.J + vec.K*vec.K)

def crossProduct3D(vector1,vector2):
    a = vector1.J*vector2.K-vector1.K*vector2.J
    b = vector1.K*vector2.I-vector1.I*vector2.K
    c = vector1.I*vector2.J-vector1.J*vector2.I
    cp = [a,b,c]
    return cp

def ang2VectorsRadian(vec1,vec2):
    numer = dotProduct3D(vec1,vec2)
    denom = vectorLength(vec1)*vectorLength(vec2)
    ang = math.acos(numer/denom)
    '''
    while ang <= -M_PI:
        ang = ang + M_2PI
    return ang
    '''
    return ang

def ang2VectorsDegree(vec1,vec2):
    return math.degrees(ang2VectorsRadian(vec1,vec2))

def ang2LinesRadian(line1,line2):
    return ang2VectorsRadian(line1.vec,line2.vec)

def ang2LinesDegrees(line1,line2):
    return ang2VectorsDegree(line1.vec,line2.vec)

def areVectorsPerpendicular(vec1,vec2):
    dP = dotProduct3D(vec1,vec2) 
    if(math.isclose(dP,0.0)):
        return True
    else:
        return False

def areLinesPerpendicular(line1,line2):
    return areVectorsPerpendicular(line1.vec,line2.vec) 

def areVectorsParallel(vec1,vec2):
    cP = crossProduct3D(vec1,vec2)
    vecLen = math.sqrt(cP[0]*cP[0] + cP[1]*cP[1] + cP[2]*cP[2])
    if(math.isclose(vecLen,0.0)):
        return True
    else:
        return False

def areLinesParallel(line1,line2):
    return areVectorsParallel(line1.vec,line2.vec)

def getDistance2DXY(point1,point2):
    d = sqrt(sqr(point2.X-point1.X) + sqr(point2.Y-point1.Y))
    return d


def getDistance2DYZ(point1,point2):
    d = sqrt(sqr(point2.Y-point1.Y) + sqr(point2.Z-point1.Z))
    return d


def getDistance2DXZ(point1,point2):
    d = sqrt(sqr(point2.X-point1.X) + sqr(point2.Z-point1.Z))
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
        
    
    

