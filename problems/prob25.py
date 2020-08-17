numsInput = input().split()
numGrid, numQuery = int(numsInput[0]), int(numsInput[1])
grid = {}
for i in range(numGrid): 
    cordName = input().split()
    grid[cordName[1]] = cordName[0]

def findDistance(x1, y1, x2, y2):
    distance = 0
    a = abs(x1-x2)
    distance += abs(a)
    ysub = int(a/2)
    b = abs(y2-y1)
    if a == b:
        return int(a * 1.5)
    if b - ysub <= 0:
        return distance
    else:
        distance = distance + b - ysub
        return distance




def toCoord(str):
    return int(str[:2]),int(str[2:])
for i in range(numQuery):
    inp = input()
    inpS = inp.split()
    x1, y1 = toCoord(grid[inpS[0]]) #coordinates for first planet
    x2, y2 = toCoord(grid[inpS[1]]) #coordinates for second planet
    print(f"{inp} {findDistance(x1, y1, x2, y2)}")
