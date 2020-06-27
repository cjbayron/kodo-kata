def isEmpty(top_left, bot_right, parkingLot):
    for i in xrange(top_left[1], bot_right[1] + 1):
        for j in xrange(top_left[0], bot_right[0] + 1):
            if parkingLot[i][j] != 0:
                return False

    return True

def canEnter(along, across, along_lim, parkingLot):
    n = 0
    for i in xrange(across[0], across[1] + 1):
        for j in xrange(0, along[0] + 1):
            if parkingLot[i][j] != 0:
                n += 1
        
        if n == 0:
            return True
        
        for j in xrange(along[1] + 1, along_lim):
            if parkingLot[i][j] != 0:
                return False
    
    return True

def parkingSpot(carDimensions, parkingLot, luckySpot):
    y1 = luckySpot[0]
    x1 = luckySpot[1]
    y2 = luckySpot[2]
    x2 = luckySpot[3]
    
    p_x = len(parkingLot[0])
    p_y = len(parkingLot)
    
    if not isEmpty([x1,y1], [x2,y2], parkingLot):
        return False

    if y2 - y1 < x2 - x1:
        return canEnter([x1, x2], [y1, y2], p_x, parkingLot)
    
    else:
        return canEnter([y1, y2], [x1, x2], p_y, parkingLot)    
