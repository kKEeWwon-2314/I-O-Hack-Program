from operator import itemgetter
import time

array = [
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
]

x = len(array[0])
y = len(array)

def inbounds(a, b):
    if (a >= 0) and (a <= y - 1) and (b >= 0) and (b <= x - 1):
        return True
    else:
        return False

def irrigationSeeker(landarray):
    irrigationlevels = []
    for i in range(y):
        for j in range(x):
            irrigated = 0

            # Self-Position
            if (landarray[i][j] == 1):
                irrigated += 1

            # North
            if inbounds(i - 1, j):
                if (landarray[i - 1][j] == 1):
                    irrigated += 1

            # Northeast
            if inbounds(i - 1, j + 1):
                if (landarray[i - 1][j + 1] == 1):
                    irrigated += 1

            # East
            if inbounds(i, j + 1):
                if (landarray[i][j + 1] == 1):
                    irrigated += 1

            # Southeast
            if inbounds(i + 1, j + 1):
                if (landarray[i + 1][j + 1] == 1):        
                    irrigated += 1
            
            # South
            if inbounds(i + 1, j):
                if (landarray[i + 1][j] == 1):        
                    irrigated += 1

            # Southwest
            if inbounds(i + 1, j - 1):
                if (landarray[i + 1][j - 1] == 1):
                    irrigated += 1
            
            # West
            if inbounds(i, j - 1):
                if (landarray[i][j - 1] == 1):
                    irrigated += 1

            # Northwest
            if inbounds(i - 1, j - 1):
                if (landarray[i - 1][j - 1] == 1):
                    irrigated += 1
            
            irrigationlevels.append([irrigated, i, j])

    return sorted(irrigationlevels, key=itemgetter(0), reverse=True)

def irrigationLevels(levels):
    counter = 0
    for level in levels:
        counter += level[0]
    return counter

def testIrrigate(x, y, array):
    ii1 = irrigationLevels(irrigationSeeker(array))
    array[x][y] = 1
    ii2 = irrigationLevels(irrigationSeeker(array))
    array[x][y] = 0
    return (ii1, ii2)

coordslist = []
for indexlist in irrigationSeeker(array):
    if (indexlist[0] == 0):
        print("(Test Irrigation in Process) Isolated cell with coordinates: (" + str(indexlist[1]) + ", " + str(indexlist[2]) + ").")
        print("Test irrigation yields an increase to", testIrrigate(indexlist[1], indexlist[2], array)[1], "from", testIrrigate(indexlist[1], indexlist[2], array)[0])
        coordslist.append((testIrrigate(indexlist[1], indexlist[2], array)[1], indexlist[1], indexlist[2]))
    elif ((array[indexlist[1]][indexlist[2]]) == 0):
        print("(Test Irrigation in Process) Dry cell with coordinates: (" + str(indexlist[1]) + ", " + str(indexlist[2]) + ") and " + str(indexlist[0]) + " water source(s).")
        print("Test irrigation yields an increase to", testIrrigate(indexlist[1], indexlist[2], array)[1], "from", testIrrigate(indexlist[1], indexlist[2], array)[0])
        coordslist.append((testIrrigate(indexlist[1], indexlist[2], array)[1], indexlist[1], indexlist[2]))
    else:
        print("Wet cell with coordinates: (" + str(indexlist[1]) + ", " + str(indexlist[2]) + ") and " + str(indexlist[0]) + " water source(s).")
        #time.sleep(0.3)



# Calculate Difference in Irrigation
print("The maximum possible irrigation level from irrigating a single community is", sorted(coordslist, key=itemgetter(0), reverse=True)[0][0], "achievable with irrigating cells: ")
for cell in coordslist:
    if (cell[0] == sorted(coordslist, key=itemgetter(0), reverse=True)[0][0]):
        print("(" + str(cell[1]) + ", " + str(cell[2]) + ")")
