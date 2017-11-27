import math

def giveLengthCoords(X1,Y1,Z1,X2,Y2,Z2):
    lineLen = math.sqrt((X2 - X1)*(X2 - X1)
                        +
                        (Y2 - Y1)*(Y2 - Y1)
                        +
                        (Z2 - Z1)*(Z2 - Z1))
    return lineLen


def giveLength2Pts(startPt,endPt):
    return giveLengthCoords(startPt.X,startPt.Y,startPt.Z,endPt.X,endPt.Y,endPt.Z)

