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

def validateLocation():
    r, c = gettingBox_XY()
    while boardList[r - 1][c - 1] != " ":
        print("this location is taken, please choose another location")
        r, c = gettingBox_XY()
    return r, c

initiateBoard()
limit = numberOfRows * numberOfCols
limitCounter = 0
while True:
    # add winning logic
    if limitCounter < limit:
        print("player 1")
        r, c = validateLocation()
        boardList[r - 1][c - 1] = "O"
        drawBoard()
        limitCounter = limitCounter + 1
    else:
        break
    if limitCounter < limit:
        print("player 2")
        r,c = validateLocation()
        boardList[r - 1][c - 1] = "X"
        drawBoard()
        limitCounter = limitCounter + 1
    else:
        break
