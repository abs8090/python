print("this is a tic tac toe python project")
boardList = []

r = 0
c = 0
numberOfRows = 0
numberOfCols = 0

withPlus = "-+"
withOutPlus = "-"

numberOfRows = int(input("enter how many rows:"))
numberOfCols = int(input("enter how many columns:"))

winningSquence = int(input("enter winning sequence:"))

def initiateBoard():
    for row in range(numberOfRows):
        rowList = []
        for col in range(numberOfCols):
            rowList.append(" ")
        boardList.append(rowList)

def drawBoard():
    rowCounter = 1
    for row in boardList:
        colCounter = 1
        for box in row:
            # draw boxes and | for each row
            if colCounter < numberOfCols :
                print("{}|".format(box), end='')
            else:
                print("{}".format(box), end='')
            colCounter = colCounter + 1
        print()
        colCounter = 1
        # end of draw boxes and | for each row
        if rowCounter < numberOfRows:
            for lineSeparator in row:
                if colCounter < numberOfCols :
                    print("{}".format(withPlus), end='')
                else:
                    print("{}".format(withOutPlus), end='')
                colCounter = colCounter + 1
        print()
        rowCounter = rowCounter + 1
def gettingBox_XY():
            r = int(input("enter which row:"))
            while r > numberOfRows:
                r = int(input("enter a valid row, max is {}\n".format(numberOfRows)))

            c = int(input("enter which column:"))
            while c > numberOfCols:
                c = int(input("enter a valid column, max is {}\n".format(numberOfCols)))
            return r, c

########################################################################

def checkWinningVerticallyUpwards(r, c, ch, whichPlayer, winningSquence):
    counter = 0
    tempRow = r
    winningSquenceCounter = 0
    flag = False

    if tempRow != 0:
        while tempRow > 0 and boardList[tempRow - 1][c] == ch:
            print("yes, it is the same as:{} {}".format(tempRow - 1 , c))
            tempRow = tempRow - 1
            if winningSquenceCounter == 0:
                winningSquenceCounter += 2
            else:
                winningSquenceCounter += 1
            if winningSquenceCounter == winningSquence:
                flag = True

    return [tempRow, c, flag]

def checkWinningVerticallyDownwards(r, c, ch, whichPlayer, winningSquence):
    counter = 0
    tempRow = r
    winningSquenceCounter = 0
    flag = False

    if tempRow < numberOfRows  - 1:
        while tempRow < numberOfRows - 1 and boardList[tempRow + 1][c] == ch:
            print("yes, it is the same as:{} {}".format(tempRow + 1 , c))
            tempRow += 1
            if winningSquenceCounter == 0:
                winningSquenceCounter += 2
            else:
                winningSquenceCounter += 1
            if winningSquenceCounter == winningSquence:
                flag = True

    return [tempRow, c, flag]

def checkWinningVertically(r, c, ch, whichPlayer, winningSquence):
    tempList = checkWinningVerticallyUpwards(r,c, ch, whichPlayer, winningSquence)
    if tempList[2]:
        return tempList[2]
    else:
        tempList2 = checkWinningVerticallyDownwards(tempList[0], tempList[1], ch, whichPlayer, winningSquence)
        return tempList2[2]

########################################################################

def checkWinningHorizontallyRight(r, c, ch, whichPlayer, winningSquence):
    tempCol = c
    winningSquenceCounter = 0
    flag = False

    if tempCol != numberOfCols - 1:
        while tempCol < numberOfCols - 1 and boardList[r][tempCol + 1] == ch:
            print("yes, it is the same as: {} {}".format(r, tempCol + 1))
            tempCol = tempCol + 1
            if winningSquenceCounter == 0:
                winningSquenceCounter += 2
            else:
                winningSquenceCounter += 1
            if winningSquenceCounter == winningSquence:
                flag = True
    return [r, tempCol, flag]

def checkWinningHorizontallyLeft(r, c, ch, whichPlayer, winningSquence):
    tempCol = c
    winningSquenceCounter = 0
    flag = False

    if tempCol != 0:
        while tempCol > 0 and boardList[r][tempCol - 1] == ch:
            print("yes, it is the same as: {} {}".format(r, tempCol - 1))
            tempCol = tempCol - 1
            if winningSquenceCounter == 0:
                winningSquenceCounter += 2
            else:
                winningSquenceCounter += 1
            if winningSquenceCounter == winningSquence:
                flag = True

    return [r, tempCol, flag]

def checkWinningHorizontally(r, c, ch, whichPlayer, winningSquence):
    tempList = checkWinningHorizontallyRight(r, c, ch, whichPlayer, winningSquence)
    if tempList[2]:
        return tempList[2]
    else:
        tempList2 = checkWinningHorizontallyLeft(tempList[0], tempList[1], ch, whichPlayer, winningSquence)
        return tempList2[2]

########################################################################

def checkWinningDaionally_UppRight(r, c, ch, whichPlayer, winningSquence):
    tempRow = r
    tempCol = c
    winningSquenceCounter = 0
    flag = False

    if tempRow != 0 and tempCol != numberOfCols - 1:
        while tempRow > 0 and tempCol < numberOfCols - 1 and boardList[tempRow - 1][tempCol + 1] == ch:
            tempRow = tempRow - 1
            tempCol = tempCol + 1
            if winningSquenceCounter == 0:
                winningSquenceCounter += 2
            else:
                winningSquenceCounter += 1
            if winningSquenceCounter == winningSquence:
                flag = True

    return [tempRow, tempCol, flag]

def checkWinningDaionally_DownLeft(r, c, ch, whichPlayer, winningSquence):
    tempRow = r
    tempCol = c
    winningSquenceCounter = 0
    flag = False

    if tempRow < numberOfRows  - 1 and tempCol != 0:
        while tempRow < numberOfRows - 1 and tempCol > 0 and boardList[tempRow + 1][tempCol - 1] == ch:
            print("yes, it is the same as: {} {}".format(tempRow + 1, tempCol - 1))
            tempRow = tempRow + 1
            tempCol = tempCol - 1
            if winningSquenceCounter == 0:
                winningSquenceCounter += 2
            else:
                winningSquenceCounter += 1
            if winningSquenceCounter == winningSquence:
                flag = True
    return [tempRow, tempCol, flag]

def checkWinningDaionally_UppRight_DownLeft(r, c, ch, whichPlayer, winningSquence):
     tempList = checkWinningDaionally_UppRight(r, c, ch, whichPlayer, winningSquence)
     if tempList[2]:
         return tempList[2]
     else:
         tempList2 = checkWinningDaionally_DownLeft(tempList[0], tempList[1], ch, whichPlayer, winningSquence)
         return tempList2[2]

########################################################################

def validateLocation():
    r, c = gettingBox_XY()
    while boardList[r - 1][c - 1] != " ":
        print("this location is taken, please choose another location")
        r, c = gettingBox_XY()
    return r, c

initiateBoard()
drawBoard()
limit = numberOfRows * numberOfCols
limitCounter = 0
while True:
    # add winning logic
    if limitCounter < limit:
        print("player 1")
        r, c = validateLocation()
        boardList[r - 1][c - 1] = "O"
        drawBoard()

        if checkWinningVertically(r - 1, c - 1, "O", 1, winningSquence):
            print("player 1 wins!!")
            break

        if checkWinningHorizontally(r - 1, c - 1, "O", 1, winningSquence):
            print("player 1 wins!!")
            break

        if checkWinningDaionally_UppRight_DownLeft(r - 1, c - 1, "O", 1, winningSquence):
            print("player 1 wins!!")
            break

        limitCounter = limitCounter + 1

    if limitCounter < limit:
        print("player 2")
        r,c = validateLocation()
        boardList[r - 1][c - 1] = "X"
        drawBoard()

        if checkWinningVertically(r - 1, c - 1, "X", 2, winningSquence):
            print("player 2 wins!!")
            break

        if checkWinningHorizontally(r - 1, c - 1, "X", 1, winningSquence):
            print("player 2 wins!!")
            break

        if checkWinningDaionally_UppRight_DownLeft(r - 1, c - 1, "X", 2, winningSquence):
            print("player 2 wins!!")
            break
        limitCounter = limitCounter + 1
    else:
        break
