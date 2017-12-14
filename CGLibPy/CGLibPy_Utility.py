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
    
    while ang <= -pi:
        ang = ang + 2*pi
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
        
def pointAtDistAlongUnitVector(startPt,unitVec,dist):
    pX = startPt.X + unitVec.I * dist
    pY = startPt.Y + unitVec.J * dist
    pZ = startPt.Z + unitVec.K * dist

    return pX,pY,pZ

def ccwWithDet(d1,d2,d3,d4):
    #Left or CCW side
    if (d1*d4 > d2*d3):
        return 1
    #Right or CW side
    if (d1*d4 < d2*d3):
        return -1
    #Right or CW side
    if ((d1*d3 < 0) or (d2*d4 < 0)):
        return -1
    #Left or CCW side
    if ((d1*d1 + d2*d2) < (d3*d3 + d4*d4)):
        return 1
    #On the line
    return 0 

def ccwOrcwXY(point0,point1,point2):
    dx1 = point1.X - point0.X
    dy1 = point1.Y - point0.Y
    dx2 = point2.X - point0.X 
    dy2 = point2.Y - point0.Y
    return ccwWithDet(dx1,dy1,dx2,dy2)

def SideOfThePointToLineXY(line,point):
    return ccwOrcwXY(line.startPt,line.endPt,point)

def ccwOrcwYZ(point0,point1,point2):
    dx1 = point1.Y - point0.Y
    dy1 = point1.Z - point0.Z
    dx2 = point2.Y - point0.Y 
    dy2 = point2.Z - point0.Z
    return ccwWithDet(dx1,dy1,dx2,dy2)

def SideOfThePointToLineYZ(line,point):
    return ccwOrcwYZ(line.startPt,line.endPt,point)

def ccwOrcwXZ(point0,point1,point2):
    dx1 = point1.X - point0.X
    dy1 = point1.Z - point0.Z
    dx2 = point2.X - point0.X 
    dy2 = point2.Z - point0.Z
    return ccwWithDet(dx1,dy1,dx2,dy2)

def SideOfThePointToLineXZ(line,point):
    return ccwOrcwXZ(line.startPt,line.endPt,point)

def square(f):
    return f * f

def arcOrSphereLineIntersection(point1, point2, arcCenter, r):
    '''
    Inspired from http://paulbourke.net/geometry/circlesphere/index.html#linesphere
    '''
    p1 = p2 = None
    u1 = u2 = None
    intersectPts = 0

    a = square(point2.X - point1.X) + square(point2.Y - point1.Y) + square(point2.Z - point1.Z)
    b = 2.0 * ((point2.X - point1.X) * (point1.X - arcCenter.X) +
               (point2.Y - point1.Y) * (point1.Y - arcCenter.Y) +
               (point2.Z - point1.Z) * (point1.Z - arcCenter.Z))

    c = (square(arcCenter.X) + square(arcCenter.Y) + square(arcCenter.Z) + square(point1.X) +
            square(point1.Y) + square(point1.Z) -
            2.0 * (arcCenter.X * point1.X + arcCenter.Y * point1.Y + arcCenter.Z * point1.Z) - square(r))

    i = b * b - 4.0 * a * c

    if i < 0.0:
        intersect = 0
    elif i == 0.0:
        # one intersection
        u1 = -b / (2.0 * a)
        intersectPts = 1

    elif i > 0.0:
        intersectPts = 2
        # first intersection
        u1 = (-b + math.sqrt(i)) / (2.0 * a)
        # second intersection
        u2 = (-b - math.sqrt(i)) / (2.0 * a)

    return intersectPts,u1,u2
    
def arcLineIntersection(line,arc):
    return arcOrSphereLineIntersection(line.startPt,line.endPt,arc.centrePt,arc.radius)
    

