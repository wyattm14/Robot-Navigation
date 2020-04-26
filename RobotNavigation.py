
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
# https://pythonprogramming.net/euclidean-distance-machine-learning-tutorial/

from math import sqrt
import sys
import time
# import time

#opening a file with an arg command
file1 = open(sys.argv[1],"r")
#initializing variables
grid = []
mangrid = []
current = []
first_line = 0
arrSize = 0
rowcounter = -1
columncounter = 0
initial_x = 0
initial_y = 0
man_x = 0
man_y = 0
ManhatLeft = 100
ManhatRight = 100
ManhatUp= 100
Manhatdown = 100
EuclidDown = 100
EuclidUp = 100
EuclidLeft = 100
EuclidRight = 100
goal = 0
goalman = 0
path_cost = 0
path_cost_man = 0
downtracker = 0
uptracker = 0
righttracker = 0
lefttracker = 0
equaltracker = 0
stringx = ""
eD = 0
eU = 0
eR= 0
eL = 0
mD = 0
mU = 0
mR= 0
mL = 0
posneg = 0
#iteration through the lines
for x in file1:
    if (rowcounter == -1):
        arrSize = int(x)
        print (arrSize)
        rowcounter += 1
    subArray = []
    #iterate through the charecters in each line
    for c in x:
        if (c == "." or c == "g" or c == "+" or c == "i"):
            subArray.append(c)
            #finding the initial state
            if (c == "i"):

                initial_x = columncounter
                initial_y = rowcounter
                man_x = columncounter
                man_y = rowcounter
                #finding the goal state
            if c == "g":
                goal_x = columncounter
                goal_y = rowcounter

            columncounter += 1
            #creating the grids
            if (len(subArray) == arrSize):
                grid.append(subArray[:])
                mangrid.append(subArray[:])
                subArray = []
                rowcounter += 1
                columncounter = 0


# for line in mangrid:
#     print (line)
fringe = []
#formula for the euclidean distance
def EuclideanDist(x,y):
    return sqrt((x-goal_x)**2+(y-goal_y)**2)
#formula for the manhattan distance
def ManhattanDist(x,y):
    return abs(x-goal_x)+abs(y-goal_y)
#putting the initial state on the fringe
def initialToFringe():
    global fringe
    fring = []
    fringe.append(initial_x)
    fringe.append(initial_y)

#moving down for the manhattan distance
def moveDownMan():
    global man_y
    global path_cost_man
    if man_y == (arrSize-1):
        print ("you cant move down anymore")
    else:
        man_y = man_y + 1
        mangrid[man_y][man_x]="o"
        path_cost_man += 1
        # print ("the manhattan path cost is: ", path_cost_man)
        # print ("MANHATTAN GRID")
        # for theline in mangrid:
        #     "".join(theline)
        #     print (theline)
        # print (grid)
        initialToFringe()
#moving up for the manhattan distance
def moveUpMan():
    global man_y
    global path_cost_man
    if (man_y == 0):
        print ("you cant move up anymore")
    else:
        man_y = man_y - 1
        mangrid[man_y][man_x]="o"
        path_cost_man += 1
        # print ("the manhattan path cost is: ", path_cost_man)
        # print ("MANHATTAN GRID")
        # for theline in mangrid:
        #     "".join(theline)
        #     print (theline)
        initialToFringe()
#moving right for the manhattan distance
def moveRightMan():
    global man_x
    global path_cost_man
    if man_x == (arrSize-1):
        print ("you cannot move right anymore")
        print (mangrid[man_y][man_x])
    if mangrid[man_y][man_x+1] == "g":
        # print ("you have reached the goal state bruh")
        # for line in mangrid:
        #     print (line)
        goalman = 1
    else:
        man_x =  man_x + 1
        mangrid[man_y][man_x]="o"
        path_cost_man += 1
        # print ("the manhattan path cost is: ", path_cost_man)
        # print ("MANHATTAN GRID")
        # for theline in mangrid:
        #     "".join(theline)
        #     print (theline)
        # print (grid)
        initialToFringe()
#moving left for the manhattan distance
def moveLeftMan():
    global man_x
    global path_cost_man
    if (man_x == 0):
        print("cannot move left anymore")
        print (mangrid[man_y][man_x])
    if mangrid[man_y][man_x-1] == "g":
        for line in mangrid:
            print (line)
        print ("you have reached the goal state left man")
        goalman = 1
    else:
        man_x = man_x - 1
        mangrid[man_y][man_x]="o"
        path_cost_man += 1
        # print ("the manhattan path cost is: ", path_cost_man)
        # print ("MANHATTAN GRID")
        # for theline in mangrid:
        #     "".join(theline)
        #     print (theline)
        initialToFringe()
#moving left for the Euclidean distance
def moveLeft():
    global initial_x
    if (initial_x == 0):
        print("cannot move left anymore")
        print (grid[initial_y][initial_x])
    if grid[initial_y][initial_x-1] == "g":
        print ("you have reached the goal state left euc")
        goal = 1
    else:
        for line in grid:
            print (line)
        initial_x = initial_x - 1
        grid[initial_y][initial_x]="o"
        global path_cost
        path_cost += 1
        print ("the euclidean path cost is: ", path_cost)
        print ("EUCLIDEAN GRID")
        for line in grid:
            print("".join(line))
        # print (EuclidLeft, "l")
        # print (EuclidUp, "u")
        # print (EuclidDown, "d")
        # print (EuclidRight, "r")
        # print ("left")
        initialToFringe()
#moving right for the Euclidean distance
def moveRight():
    global initial_x
    if initial_x == (arrSize-1):
        print ("you cannot move right anymore")
        print (grid[initial_y][initial_x])
    if grid[initial_y][initial_x+1] == "g":
        print (initial_y,initial_x, "coordinates")
        print ("you have reached the goal state bitch")
        goal = 1
    else:
        for line in grid:
            print (line)
        initial_x =  initial_x + 1
        grid[initial_y][initial_x]="o"
        global path_cost
        path_cost += 1
        print ("the euclidean path cost is: ", path_cost)
        print ("EUCLIDEAN GRID")
        for line in grid:
            print ("".join(line))
        # print (EuclidLeft, "l")
        # print (EuclidUp, "u")
        # print (EuclidDown, "d")
        # print (EuclidRight, "r")
        # print ("right")
        initialToFringe()
#moving up for the Euclidean distance
def moveUp():
    global initial_y
    if (initial_y == 0):
        print ("you cant move up anymore")
    else:
        initial_y = initial_y - 1
        grid[initial_y][initial_x]="o"
        global path_cost
        path_cost += 1
        print ("the euclidean path cost is: ", path_cost)
        print ("EUCLIDEAN GRID")
        for line in grid:
            print ("".join(line))
        # print (EuclidLeft, "l")
        # print (EuclidUp, "u")
        # print (EuclidDown, "d")
        # print (EuclidRight, "r")
        # print ("up")
        initialToFringe()
#moving down for the Euclidean distance
def moveDown():
    global initial_y
    if initial_y == (arrSize-1):
        print ("you cant move down anymore")
    else:
        initial_y = initial_y + 1
        grid[initial_y][initial_x]="o"
        global path_cost
        path_cost += 1
        print ("the euclidean path cost is: ", path_cost)
        print ("EUCLIDEAN GRID")
        for line in grid:
            print ("".join(line))
        # print (EuclidLeft, "l")
        # print (EuclidUp, "u")
        # print (EuclidDown, "d")
        # print (EuclidRight, "r")
        # print ("down")
        initialToFringe()
#evaluating the euclidean distances for up down left and right, given it is a legal move.
def evaluateEuclid():
    global initial_x
    global initial_y
    global EuclidLeft
    global EuclidDown
    global EuclidUp
    global EuclidRight
    global posneg
    # print ("HEY WE IN EVALEUCLID")

    #if it is in the initial state
    if grid[initial_y][initial_x] == "i":
        # print("In the initial state")
        if initial_x -1 >= 0:
            # print("In the checking left ")
            if (grid[initial_y][initial_x-1] == '.'):
                leftmove = initial_x - 1
                eL = EuclidLeft
                EuclidLeft = EuclideanDist(leftmove,initial_y)
                posneg = EuclidLeft - eL
                # print ("this is Euclid left: ", EuclidLeft)
        if initial_x + 1<= arrSize-1:
            # print("In the checking right ")
            if (grid[initial_y][initial_x+1] == '.'):
                rightmove = initial_x + 1
                eR = EuclidRight
                EuclidRight = EuclideanDist(rightmove,initial_y)
                posneg = EuclidRight - eR
                # print ("this is Euclid right: ", EuclidRight)
        if initial_y + 1<= arrSize -1:
            # print("In the checking down ")
            if (grid[initial_y+1][initial_x] == '.'):
                downmove = initial_y + 1
                eD = EuclidDown
                EuclidDown = EuclideanDist(initial_x,downmove)
                posneg = EuclidDown -eD
                # print ("this is Euclid down: ", EuclidDown)
        if initial_y - 1>= 0:
            # print("In the checking up ")
            if (grid[initial_y-1][initial_x] == '.'):
                eU = EuclidUp
                upmove = initial_y - 1
                EuclidUp = EuclideanDist(initial_x,upmove)
                posneg = EuclidUp - eU
    # not in the initial state
    if grid[initial_y][initial_x] != "i":
        if initial_x - 1>= 0:
            # print("In the checking left ")
            if (grid[initial_y][initial_x-1] == '.'):
                leftmove = initial_x - 1
                eL = EuclidLeft
                EuclidLeft = EuclideanDist(leftmove,initial_y)
                posneg = EuclidLeft - eL
                # print ("this is Euclid left: ", EuclidLeft)
        if initial_x + 1<= arrSize -1:
            # print("In the checking right ")
            print (grid [initial_y][initial_x+1] )
            if (grid[initial_y][initial_x+1] == '.'):
                rightmove = initial_x + 1
                eR = EuclidRight
                EuclidRight = EuclideanDist(rightmove,initial_y)
                posneg = EuclidRight - eR
                # print ("this is Euclid right: ", EuclidRight)
        # print (initial_y, "This is initial y bruh")
        if initial_y+1<= arrSize-1:
            # print("In the checking down ")
            if (grid[initial_y+1][initial_x] == '.'):
                downmove = initial_y + 1
                eD = EuclidDown
                EuclidDown = EuclideanDist(initial_x,downmove)
                posneg = EuclidDown - eD
                # print ("this is Euclid down: ", EuclidDown)
        if initial_y - 1>= 0:
            # print("In the checking up ")
            if (grid[initial_y-1][initial_x] == '.'):
                eU = EuclidUp
                upmove = initial_y - 1
                EuclidUp = EuclideanDist(initial_x,upmove)
                posneg = EuclidUp - eU
                # print ("this is Euclid up: ", EuclidUp)

# def seeWhatsEqual():
#     if equaltracker > 0:
#         if EuclidUp == EuclidRight and EuclidUp != 100:
#             # print ("up and right are equal")
#         elif EuclidUp == EuclidLeft and EuclidUp != 100:
#             # print ("up and left are equal")
#         elif EuclidDown == EuclidRight and EuclidDown != 100:
#             # print ("down and right are equal")
#         elif EuclidDown == EuclidLeft and EuclidDown != 100:
#             # print ("down and left are equal")
#         elif EuclidLeft == EuclidRight and EuclidRight != 100:
#             # print ("left and right are equal")
#     else:
#         print ("nevermind, nothing is equal")

#evaluating the manhattan distances for up, down, left =, and right
def evaluateMan():
    global man_x
    global man_y
    global ManhatLeft
    global Manhatdown
    global ManhatUp
    global ManhatRight
    # print(mangrid)
    # for thing in mangrid:
    #     print("".join(thing))
    # print(man_y, " man_y")
    # time.sleep(.5)
    # print(man_x, " man_x")

    #checking if its in the initial state
    if mangrid[man_y][man_x] == "i":
        if man_x -1 >= 0:
            if (mangrid[man_y][man_x-1] == '.'):
                leftmoveman = man_x - 1
                mL = ManhatLeft
                ManhatLeft = ManhattanDist(leftmoveman,man_y)
                # print ("this is Manhattan left: ", ManhatLeft)
        if man_x + 1<= arrSize-1:
            if (mangrid[man_y][man_x+1] == '.'):
                # print ("RIGHHHHTT")
                rightmoveman = man_x + 1
                mR = ManhatRight
                ManhatRight = ManhattanDist(rightmoveman,man_y)
                # print ("this is Manhattan right: ", ManhatRight)
        if man_y + 1<= arrSize -1:
            if (mangrid[man_y+1][man_x] == '.'):
                downmoveman = man_y + 1
                mD = Manhatdown
                Manhatdown = ManhattanDist(man_x,downmoveman)
                # print ("this is Manhattan down: ", Manhatdown)
        if man_y - 1>= 0:
            if (mangrid[man_y-1][man_x] == '.'):
                # print("LEFTTTTT")
                mU = ManhatUp
                upmoveman = man_y - 1
                ManhatUp = ManhattanDist(man_x,upmoveman)
                # print ("this is Manhattan up: ", ManhatUp)
    #if it is not in the initial state
    if mangrid[man_y][man_x] != "i":
        if man_x - 1>= 0:
            if (mangrid[man_y][man_x-1] == '.'):
                leftmoveman = man_x - 1
                mL = ManhatLeft
                ManhatLeft = ManhattanDist(leftmoveman,man_y)
                # print ("this is Euclid left: ", ManhatLeft)
        if man_x + 1<= arrSize -1:
            if (mangrid[man_y][man_x+1] == '.'):
                rightmoveman = man_x + 1
                mR = ManhatRight
                ManhatRight = ManhattanDist(rightmoveman,man_y)
                # print ("this is Manhattan right: ", ManhatRight)
        if man_y + 1<= arrSize-1:
            if (mangrid[man_y+1][man_x] == '.' ):
                downmoveman = man_y + 1
                mD = Manhatdown
                Manhatdown = ManhattanDist(man_x,downmoveman)
                # print ("this is Manhattan down: ", Manhatdown)
        if man_y - 1>= 0:
            if (mangrid[man_y-1][man_x] == '.'):
                mU = ManhatUp
                upmoveman = man_y - 1
                ManhatUp = ManhattanDist(man_x,upmoveman)
                # print ("this is Manhattan up: ", ManhatUp)

# evaluting which manhattan distances are the lowest, simultaneously checking if the goal state has been reached
def letsmoveman():
    # time.sleep(.5)
    # for line in mangrid:
    #     print (line)
    #
    # print ("end here")
    global goalman
    while (goalman != 1):
        evaluateMan()
        #for the left sude
        if (ManhatLeft != 100):
            if man_x-1 >= 0:
                if (ManhatLeft < Manhatdown and ManhatLeft < ManhatUp and ManhatLeft < ManhatRight) and mangrid[man_y][man_x-1] != "+":
                    if (mangrid[man_y][man_x-1] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        print ("the manhattan path cost is: ", path_cost_man)
                        print ("MANHATTAN GRID")
                        for theline in mangrid:
                            print("".join(theline))
                        goalman = 1
                        break
                    moveLeftMan()
                    evaluateMan()
                if man_x - 1 >= 0:
                    if (ManhatLeft == ManhatUp or ManhatLeft == Manhatdown or ManhatLeft == ManhatRight and mangrid[man_y][man_x-1] != "+"):
                        if (mangrid[man_y][man_x-1] == "g"):
                            print ("THE GOAL HAS BEEN REACHED: ")
                            goalman = 1
                            print ("the manhattan path cost is: ", path_cost_man)
                            print ("MANHATTAN GRID")
                            for theline in mangrid:
                                print("".join(theline))
                            break
                        moveLeftMan()
                        evaluateMan()
        # for the up movement
        if (ManhatUp != 100):
            if man_y - 1>= 0 and mangrid[man_y-1][man_x] != "+":
                if (ManhatUp < ManhatLeft and ManhatUp < Manhatdown and ManhatUp < ManhatRight):
                    if (mangrid[man_y-1][man_x] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        print ("the manhattan path cost is: ", path_cost_man)
                        print ("MANHATTAN GRID")
                        for theline in mangrid:
                            print("".join(theline))
                        goalman = 1
                        break
                    moveUpMan()
                    evaluateMan()
                if man_y - 1>= 0 and mangrid[man_y-1][man_x] != "+":
                    if (ManhatUp == ManhatLeft or ManhatUp == Manhatdown or ManhatUp == ManhatRight):
                        if (mangrid[man_y-1][man_x] == "g"):
                            print ("THE GOAL HAS BEEN REACHED: ")
                            print ("the manhattan path cost is: ", path_cost_man)
                            print ("MANHATTAN GRID")
                            for theline in mangrid:
                                print("".join(theline))
                            goalman = 1
                            break
                        moveUpMan()
                        evaluateMan()
        # for the down movement
        if (Manhatdown != 100):
            # print ("good here")
            if man_y + 1 <= arrSize -1:
                # print ("good here 2")
                # print (ManhatUp, "up")
                # print (ManhatLeft, "left")
                # print (Manhatdown, "down")
                # print (ManhatRight, "right")
                if (Manhatdown < ManhatLeft and Manhatdown < ManhatUp and Manhatdown < ManhatRight and mangrid[man_y+1][man_x] != "+"):
                    # print ("good here 3")
                    if (mangrid[man_y+1][man_x] == "g"):
                        print ("good here 4")
                        print ("THE GOAL HAS BEEN REACHED: ")
                        print ("the manhattan path cost is: ", path_cost_man)
                        print ("MANHATTAN GRID")
                        for theline in mangrid:
                            print("".join(theline))
                        goalman = 1
                        break
                    moveDownMan()
                    evaluateMan()
                if man_y + 1 <= arrSize -1:
                    if (Manhatdown == ManhatLeft or Manhatdown == ManhatUp or Manhatdown == ManhatRight and mangrid[man_y+1][man_x] != "+"):
                        if (mangrid[man_y+1][man_x] == "g"):
                            print ("THE GOAL HAS BEEN REACHED: ")
                            print ("the manhattan path cost is: ", path_cost_man)
                            print ("MANHATTAN GRID")
                            for theline in mangrid:
                                print("".join(theline))
                            goalman = 1
                            break
                        moveDownMan()
                        evaluateMan()
        # for the right movement
        if (ManhatRight != 100):
            if man_x + 1 <= arrSize - 1:
                if (ManhatRight < ManhatUp and ManhatRight < Manhatdown and ManhatRight < ManhatLeft and mangrid[man_y][man_x+1] != "+"):
                    if (mangrid[man_y][man_x+1] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        print ("the manhattan path cost is: ", path_cost_man)
                        print ("MANHATTAN GRID")
                        for theline in mangrid:
                            print("".join(theline))
                        goalman = 1
                        break
                    moveRightMan()
                    evaluateMan()
                elif man_x + 1 <= arrSize - 1:
                    if (ManhatRight == ManhatUp or ManhatRight == Manhatdown or ManhatRight == ManhatLeft and mangrid[man_y][man_x+1] != "+"):

                        if (mangrid[man_y][man_x+1] == "g"):
                            print ("THE GOAL HAS BEEN REACHED: ")
                            print ("the manhattan path cost is: ", path_cost_man)
                            print ("MANHATTAN GRID")
                            for theline in mangrid:
                                print("".join(theline))
                            goalman = 1
                            break
                        moveRightMan()
                        evaluateMan()

        letsmoveman()
#evaulating the lowest euclidean distances and making movements based on that, simultaneously checking if the goal has been reached
def letsmove():
    global stringx
    global goal
    global equaltracker
    global downtracker
    global lefttracker
    global righttracker
    global uptracker
    while (goal != 1):
        # time.sleep(.5)
        # print ("FIX THIS RECURSIONNNNNN")
        evaluateEuclid()
        # print (EuclidUp, "up")
        # print (EuclidDown, "down")
        # print (EuclidRight, "right")
        # print (EuclidLeft, "left")
        # for line in grid:
        #     print (line)

        # for down movements
        if (EuclidDown != 100):
            if (EuclidDown < EuclidLeft and EuclidDown < EuclidUp and EuclidDown < EuclidRight and grid[initial_y+1][initial_x] != "+"):
                # print (initial_x, "X")
                # print (initial_y, "Y")
                if initial_y + 1<= arrSize-1:

                    if (grid[initial_y+1][initial_x] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        goal = 1
                        print ("the euclidean path cost is: ", path_cost)
                        print ("THIS IS THE EUCLIDEAN GRID")
                        for line in grid:
                            print("".join(line))
                        break
                    moveDown()
                    evaluateEuclid()
                    downtracker += 1
                if downtracker == 1 and righttracker == 0 and lefttracker == 0 and uptracker == 0:
                    # print ("down was the first move")
                    stingx = "down"
            elif (EuclidDown == EuclidLeft or EuclidDown == EuclidUp or EuclidDown == EuclidRight and grid[initial_y+1][initial_x] != "+"):
                equaltracker += 1
                # seeWhatsEqual()
                if initial_y + 1<= arrSize-1:

                    if (grid[initial_y+1][initial_x] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        goal = 1
                        print ("the euclidean path cost is: ", path_cost)
                        print ("THIS IS THE EUCLIDEAN GRID")
                        for line in grid:
                            print("".join(line))
                        break

                    moveDown()
                    evaluateEuclid()
                    downtracker += 1

                if downtracker == 1 and righttracker == 0 and lefttracker == 0 and uptracker == 0:
                    # print ("down was the first move")
                    stringx = "down"

        # for left movements
        if (EuclidLeft != 100):
            if (EuclidLeft < EuclidDown and EuclidLeft < EuclidUp and EuclidLeft < EuclidRight and grid[initial_y][initial_x-1] != "+"):

                if initial_x -1 >= 0:

                    if (grid[initial_y][initial_x-1] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        goal = 1
                        print ("the euclidean path cost is: ", path_cost)
                        print ("THIS IS THE EUCLIDEAN GRID")
                        for line in grid:
                            print("".join(line))
                        break
                    moveLeft()
                    evaluateEuclid()
                    lefttracker += 1
                    if lefttracker == 1 and righttracker == 0 and downtracker == 0 and uptracker == 0:
                        # print ("left was the first move")
                        stringx = "left"
            elif (EuclidLeft == EuclidUp or EuclidLeft == EuclidDown or EuclidLeft == EuclidRight and grid[initial_y][initial_x-1] != "+"):
                equaltracker += 1

                if initial_x -1 >= 0:

                # seeWhatsEqual()
                    if (grid[initial_y][initial_x-1] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        goal = 1
                        print ("the euclidean path cost is: ", path_cost)
                        print ("THIS IS THE EUCLIDEAN GRID")
                        for line in grid:
                            print("".join(line))
                        break
                    moveLeft()
                    evaluateEuclid()
                    lefttracker += 1
                    if lefttracker == 1 and righttracker == 0 and downtracker == 0 and uptracker == 0:
                        # print ("left was the first move")
                        stringx = "left"
        #for up movements
        if (EuclidUp != 100):
            if (EuclidUp < EuclidLeft and EuclidUp < EuclidDown and EuclidUp < EuclidRight and grid[initial_y-1][initial_x] != "+"):

                if initial_y - 1 >= 0:

                    if (grid[initial_y-1][initial_x] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        goal = 1
                        print ("the euclidean path cost is: ", path_cost)
                        print ("THIS IS THE EUCLIDEAN GRID")
                        for line in grid:
                            print("".join(line))
                        break
                    moveUp()
                    evaluateEuclid()
                    uptracker += 1
                    if uptracker == 1 and righttracker == 0 and downtracker == 0 and lefttracker == 0:
                        # print ("up was the first move")
                        stringx = "up"
            elif (EuclidUp == EuclidLeft or EuclidUp == EuclidDown or EuclidUp == EuclidRight and grid[initial_y-1][initial_x] != "+"):
                equaltracker += 1

                if initial_y - 1>= 0:

                # seeWhatsEqual()
                    if (grid[initial_y-1][initial_x] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        goal = 1
                        print ("the euclidean path cost is: ", path_cost)
                        print ("THIS IS THE EUCLIDEAN GRID")
                        for line in grid:
                            print("".join(line))
                        break
                    moveUp()
                    evaluateEuclid()
                    uptracker += 1
                    if uptracker == 1 and righttracker == 0 and downtracker == 0 and lefttracker == 0:
                        # print ("up was the first move")
                        stringx = "up"

        #for right movements
        if (EuclidRight != 100):
            if (EuclidRight < EuclidUp and EuclidRight < EuclidDown and EuclidRight < EuclidLeft and grid[initial_y][initial_x+1] != "+"):

                if initial_x + 1 <= arrSize-1:

                    if (grid[initial_y][initial_x+1] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        goal = 1
                        print ("the euclidean path cost is: ", path_cost)
                        print ("THIS IS THE EUCLIDEAN GRID")
                        for line in grid:
                            print("".join(line))
                        break
                    moveRight()
                    evaluateEuclid()
                    righttracker += 1
                    if righttracker == 1 and uptracker == 0 and downtracker == 0 and lefttracker == 0:
                        # print ("up was the first move")
                        stringx = "right"
            elif (EuclidRight == EuclidUp or EuclidRight == EuclidDown or EuclidRight == EuclidLeft and grid[initial_y][initial_x+1] != "+"):
                equaltracker += 1
                # seeWhatsEqual()
                if initial_x + 1 <= arrSize-1:

                    if (grid[initial_y][initial_x+1] == "g"):
                        print ("THE GOAL HAS BEEN REACHED: ")
                        goal = 1
                        print ("the euclidean path cost is: ", path_cost)
                        print ("THIS IS THE EUCLIDEAN GRID")
                        for line in grid:
                            print("".join(line))
                        break
                    moveRight()
                    evaluateEuclid()
                    righttracker += 1
                    if righttracker == 1 and uptracker == 0 and downtracker == 0 and lefttracker == 0:
                        # print ("up was the first move")
                        stringx = "right"
        letsmove()

#running euclidean first
letsmove()
print ("\nTime for the next search grid: \n")
#running manhattan next
letsmoveman()

file1.close()
