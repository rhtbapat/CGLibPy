import math

def distCoords(X1,Y1,Z1,X2,Y2,Z2):
    return math.sqrt(math.pow(X2-X1,2)+math.pow(Y2-Y1,2)+math.pow(Z2-Z1,2))

def dist2Pts(startPt,endPt):
    return distCoords(startPt.X,startPt.Y,startPt.Z,endPt.X,endPt.Y,endPt.Z)

def dotProduct3DIJK(I1,J1,K1,I2,J2,K2):
    dp = I1*I2 + J1*J2 + K1*K2 
    return dp

def dotProduct3D(vector1,vector2):
    return dotProduct3DIJK(vector1.I,vector1.J,vector1.K,vector2.I,vector2.J,vector2.K)

def vectorLengthIJK(I,J,K):
    return math.sqrt(I*I + J*J + K*K)

def vectorLength(vec):
    return vectorLengthIJK(vec.I,vec.J,vec.K)

def crossProduct3DIJK(I1,J1,K1,I2,J2,K2):
    a = J1*K2-K1*J2
    b = K1*I2-I1*K2
    c = I1*J2-J1*I2
    cp = [a,b,c]
    return cp

def crossProduct3D(vector1,vector2):
    return crossProduct3DIJK(vector1.I,vector1.J,vector1.K,vector2.I,vector2.J,vector.K)

def ang2VectorsRadian(vec1,vec2):
    numer = dotProduct3D(vec1,vec2)
    denom = vectorLength(vec1)*vectorLength(vec2)
    ang = math.acos(numer/denom)
    
    while ang <= -math.pi:
        ang = ang + 2*math.pi
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

def areVectorsParallelIJK(I1,J1,K1,I2,J2,K2):
    cP = crossProduct3DIJK(I1,J1,K1,I2,J2,K2)
    vecLen = math.sqrt(cP[0]*cP[0] + cP[1]*cP[1] + cP[2]*cP[2])
    if(math.isclose(vecLen,0.0)):
        return True
    else:
        return False

def areVectorsParallel(vec1,vec2):
    return areVectorsParallelIJK(vec1.I,vec1.J,vec1.K,vec2.I,vec2.J,vec2.K)

def areLinesParallelCoordinates(point1,point2,point3,point4):
    I1 = point2[0]-point1[0]
    J1 = point2[1]-point1[1]
    K1 = point2[2]-point1[2]
    I2 = point4[0]-point3[0]
    J2 = point4[1]-point3[1]
    K2 = point4[2]-point3[2]
    return areVectorsParallelIJK(I1,J1,K1,I2,J2,K2)

def areLinesParallel(line1,line2):
    return areVectorsParallel(line1.vec,line2.vec)

def getDistance2DXY(point1,point2):
    d = sqrt(sqr(point2.X-point1.X) + sqr(point2.Y-point1.Y))
    return d

def arePointsCollinear(pt1,pt2,pt3):
    I1 = pt2.X - pt1.X
    J1 = pt2.Y - pt2.Y
    K1 = pt2.Z - pt2.Z
    I2 = pt3.X - pt2.X
    J2 = pt3.Y - pt2.Y
    K2 = pt3.Z - pt2.Z
    return areVectorsParallelIJK(I1,J1,K1,I2,J2,K2)

def vectorProjectOnVector(sourceVec,targetVec):
    ang = ang2VectorsRadian(sourceVec,targetVec)
    normVec2 = targetVec.unitVector()
    vecLen = vectorLength(sourceVec)
    val = vecLen*math.cos(ang)
    return (normVec2.I*val,normVec2.J*val,normVec2.K*val)

def lineProjectOnLine(sourceLine,targetLine):
    return vectorProjectOnVector(sourceLine.vec,targetLine.vec)

def getDistance2DYZ(point1,point2):
    d = sqrt(sqr(point2.Y-point1.Y) + sqr(point2.Z-point1.Z))
    return d

def getDistance2DXZ(point1,point2):
    d = sqrt(sqr(point2.X-point1.X) + sqr(point2.Z-point1.Z))
    return d

def lineLineIntersection3DCoordinatesParameters(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    p13X = X1 - X3
    p13Y = Y1 - Y3
    p13Z = Z1 - Z3
    p43X = X4 - X3
    p43Y = Y4 - Y3
    p43Z = Z4 - Z3

    if (math.isclose(math.fabs(p43X),0.0) 
        and math.isclose(math.fabs(p43Y),0.0) 
        and math.isclose(math.fabs(p43Z),0.0)) :
        return False,-1,-1 #bool,u,v

    p21X = X2 - X1
    p21Y = Y2 - Y1
    p21Z = Z2 - Z1

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

def lineLineIntersection3DPointsParameters(p1,p2,p3,p4):
    return lineLineIntersection3DCoordinatesParameters(p1.X,p1.Y,p1.Z,p2.X,p2.Y,p2.Z,p3.X,p3.Y,p3.Z,p4.X,p4.Y,p4.Z)

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
    '''#Right or CW side
    if ((d1*d3 < 0) or (d2*d4 < 0)):
        return -1
    #Left or CCW side
    if ((d1*d1 + d2*d2) < (d3*d3 + d4*d4)):
        return 1'''
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

def arcThroughThreePoints(pt1,pt2,pt3):
    arcPossible = False
    centre = None
    radius = 0
    sweepAng = 0
    startPt = None
    endPt = None

    tempPt1 = pt1
    tempPt2 = pt2
    tempPt3 = pt3

    I1 = pt2.X - pt1.X
    J1 = pt2.Y - pt2.Y
    K1 = pt2.Z - pt2.Z
    I2 = pt3.X - pt2.X
    J2 = pt3.Y - pt2.Y
    K2 = pt3.Z - pt2.Z

    midPt1X = (pt1.X+pt2.X)/2
    midPt1Y = (pt1.Y+pt2.Y)/2
    midPt1Z = (pt1.Z+pt2.Z)/2

    midPt2X = (pt2.X+pt3.X)/2
    midPt2Y = (pt2.Y+pt3.Y)/2
    midPt2Z = (pt2.Z+pt3.Z)/2

    selectedPlane = "XY"
    tempVecLen = math.sqrt(square(I1)+square(J1))
    tempVec1 = [I1/tempVecLen,J1/tempVecLen,0]
    tempPerpVec1 = [J1/tempVecLen,I1/tempVecLen,0]
    tempVec2Len = math.sqrt(square(I2)+square(J2))
    tempVec2 = [I2/tempVecLen,J2/tempVecLen,0]
    tempPerpVec2 = [J2/tempVecLen,I2/tempVecLen,0]
    tempPt1.Z = 0
    tempPt2.Z = 0
    tempPt3.Z = 0

    if (areVectorsParallelIJK(I1,J1,K1,I2,J2,K2) != True):
        return False,None
    else:
        cP = crossProduct3DIJK(I1,J1,K1,I2,J2,K2)
        if (math.isclose(cP.J,0) and math.isclose(cP.K,0)):
            selectedPlane = "YZ"
            tempVecLen = math.sqrt(square(J1)+square(K1))
            tempVec1 = [0,J1/tempVecLen,K1/tempVecLen]
            tempPerpVec1 = [0,K1/tempVecLen,J1/tempVecLen]
            tempVec2Len = math.sqrt(square(J2)+square(K2))
            tempVec2 = [0,J2/tempVecLen,K2/tempVecLen]
            tempPerpVec2 = [0,K2/tempVecLen,J2/tempVecLen]
            tempPt1.X = 0
            tempPt2.X = 0
            tempPt3.X = 0
        elif (math.isclose(cP.I,0) and math.isclose(cP.K,0)):
            selectedPlane = "XZ"
            tempVecLen = math.sqrt(square(I1)+square(K1))
            tempVec1 = [I1/tempVecLen,0,K1/tempVecLen]
            tempPerpVec1 = [K1/tempVecLen,0,I1/tempVecLen]
            tempVec2Len = math.sqrt(square(I2)+square(K2))
            tempVec2 = [I2/tempVecLen,0,K2/tempVecLen]
            tempPerpVec2 = [K2/tempVecLen,0,I2/tempVecLen]
            tempPt1.Y = 0
            tempPt2.Y = 0
            tempPt3.Y = 0
    
    tempDist = 1
    tempPt1X = midPt1X + tempPerpVec1[0]*tempDist
    tempPt1Y = midPt1Y + tempPerpVec1[1]*tempDist
    tempPt1Z = midPt1Z + tempPerpVec1[2]*tempDist

    tempPt2X = midPt2X + tempPerpVec2[0]*tempDist
    tempPt2Y = midPt2Y + tempPerpVec2[1]*tempDist
    tempPt2Z = midPt2Z + tempPerpVec2[2]*tempDist

    inter,u,v = lineLineIntersection3DCoordinatesParameters(midPt1X,midPt1Y,midPt1Z,tempPt1X,tempPt1Y,tempPt1Z,midPt2X,midPt2Y,midPt2Z,tempPt2X,tempPt2Y,tempPt2Z)
    if (inter):
        interPtX = midPt1X + (tempPt1X-midPt1X)*u   
        interPtY = midPt1Y + (tempPt1Y-midPt1Y)*u
        interPtZ = midPt1Z + (tempPt1Z-midPt1Z)*u

        tempInter,tempU,tempV = lineLineIntersection3DCoordinatesParameters(tempPt1.X,tempPt1.Y,tempPt1.Z,interPtX,interPtY,interPtZ,tempPt2.X,tempPt2.Y,tempPt2.Z,tempPt3.X,tempPt3.Y,tempPt3.Z)
        tempInterPtX = tempPt3.X + (interPtX - tempPt3.X)*tempU
        tempInterPtY = tempPt3.Y + (interPtY - tempPt3.Y)*tempU
        tempInterPtZ = tempPt3.Z + (interPtZ - tempPt3.Z)*tempU

        dist1 = distCoords(tempPt2.X,tempPt2.Y,tempPt2.Z,tempPt3.X,tempPt3.Y,tempPt3.Z)
        dist2 = distCoords(tempPt2.X,tempPt2.Y,tempPt2.Z,tempInterPtX,tempInterPtY,tempInterPtZ)
        ratio1 = dist2/dist1
        dist3 = distCoords(tempPt1.X,tempPt1.Y,tempPt1.Z,tempInterPtX,tempInterPtY,tempInterPtZ)
        dist4 = distCoords(tempPt1.X,tempPt1.Y,tempPt1.Z,interPtX,interPtY,interPtZ)
        ratio2 = dist4/dist3

        actualPt23X = pt2.X + (pt3.X-pt2.X)*ratio1
        actualPt23Y = pt2.Y + (pt3.Y-pt2.Y)*ratio1
        actualPt23Z = pt2.Z + (pt3.Z-pt2.Z)*ratio1

        centreArcX = pt1.X + (actualPt23X-pt1.X)*ratio2
        centreArcY = pt1.Y + (actualPt23Y-pt1.Y)*ratio2
        centreArcZ = pt1.Z + (actualPt23Z-pt1.Z)*ratio2

        radius = distCoords(centreArcX,centreArcY,centreArcZ,pt1.X,pt1.Y,pt1.Z)
    else:
        return False,None

def lineLineIntersection2DCoordinates(x1,y1,x2,y2,x3,y3,x4,y4):
    det = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if math.isclose(det,0):
        return False,0,0 #Bool,u,v
    u = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3))/det
    v = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3))/det

    return True,u,v

def lineLineIntersection2DXYPoints(point1,point2,point3,point4):
    return lineLineIntersection2DCoordinates(point1.X,point1.Y,point2.X,point2.Y,point3.X,point3.Y,point4.X,point4.Y)
            
def lineLineIntersection2DXY(line1,line2):
    return lineLineIntersection2DXYPoints(line1.startPt,line1.endPt,line2.startPt,line2.endPt)

def lineLineIntersection2DYZPoints(point1,point2,point3,point4):
    return lineLineIntersection2DCoordinates(point1.Y,point1.Z,point2.Y,point2.Z,point3.Y,point3.Z,point4.Y,point4.Z)
            
def lineLineIntersection2DYZ(line1,line2):
    return lineLineIntersection2DYZPoints(line1.startPt,line1.endPt,line2.startPt,line2.endPt)

def lineLineIntersection2DXZPoints(point1,point2,point3,point4):
    return lineLineIntersection2DCoordinates(point1.X,point1.Z,point2.X,point2.Z,point3.X,point3.Z,point4.X,point4.Z)
            
def lineLineIntersection2DXZ(line1,line2):
    return lineLineIntersection2DXYPoints(line1.startPt,line1.endPt,line2.startPt,line2.endPt)

def lineLineIntersection2D(line1,line2,plane="XY"):
    if plane == "XY":
        return lineLineIntersection2DXY(line1,line2)
    elif plane == "YZ":
        return lineLineIntersection2DYZ(line1,line2)
    else:
        return lineLineIntersection2DXZ(line1,line2)

def lineLineIntersection3DUsingCrossProduct(line1,line2):
    selectedPlane = "XY"
    parallelOnAllPlanes = 0

    if(line1.startPt.samePoint(line2.startPt)):
        return True,0.0,0.0
    elif (line1.startPt.samePoint(line2.endPt)):
        return True,0.0,1.0
    elif (line1.endPt.samePoint(line2.startPt)):
        return True,1.0,0.0
    elif (line1.endPt.samePoint(line2.endPt)):
        return True,1.0,1.0

    tempLine1 = line1
    tempLine2 = line2
    # Eliminate XY plane
    tempPt1 = [line1.startPt.X,line1.startPt.Y,0]
    tempPt2 = [line1.endPt.X,line1.endPt.Y,0]
    tempPt3 = [line2.startPt.X,line2.startPt.Y,0]
    tempPt4 = [line2.endPt.X,line2.endPt.Y,0]
    if areLinesParallelCoordinates(tempPt1,tempPt2,tempPt3,tempPt4):
        if parallelOnAllPlanes == 0:
            parallelOnAllPlanes = parallelOnAllPlanes + 1
        selectedPlane = "YZ"
    tempPt1 = [0,line1.startPt.Y,line1.startPt.Z]
    tempPt2 = [0,line1.endPt.Y,line1.endPt.Z]
    tempPt3 = [0,line2.startPt.Y,line2.startPt.Z]
    tempPt4 = [0,line2.endPt.Y,line2.endPt.Z]
    if areLinesParallelCoordinates(tempPt1,tempPt2,tempPt3,tempPt4):
        if parallelOnAllPlanes == 1:
            parallelOnAllPlanes = parallelOnAllPlanes + 1
        selectedPlane = "XZ"
    # Eliminate XZ plane
    tempPt1 = [line1.startPt.X,0,line1.startPt.Z]
    tempPt2 = [line1.endPt.X,0,line1.endPt.Z]
    tempPt3 = [line2.startPt.X,0,line2.startPt.Z]
    tempPt4 = [line2.endPt.X,0,line2.endPt.Z]
    if areLinesParallelCoordinates(tempPt1,tempPt2,tempPt3,tempPt4):
        if parallelOnAllPlanes == 2:
            return False,0,0

    return lineLineIntersection2D(line1,line2,selectedPlane)



    

