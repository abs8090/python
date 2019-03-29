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
            rowList.append("A")
        boardList.append(rowList)

def drawBoard():
    rowCounter = 0
    for row in boardList:
        colCounter = 0
        for box in row:
            # draw boxes and | for each row
            if colCounter < numberOfRows - 1:
                print("{}|".format(box), end='')
            else:
                print("{}".format(box), end='')
            colCounter = colCounter + 1
        print()
        # end of draw boxes and | for each row
        colCounter = 0
        if rowCounter < numberOfRows - 1:
            for lineSeparator in row:
                if colCounter < numberOfRows - 1:
                    print("{}".format(withPlus), end='')
                else:
                    print("{}".format(withOutPlus), end='')
                colCounter = colCounter + 1
            print()
        rowCounter = rowCounter + 1



initiateBoard()
limit = numberOfRows + numberOfCols
limitCounter = 0
while True:
    if limitCounter < limit:
        drawBoard()
        print("player 1")
        r = int(input("enter which row:"))
        c = int(input("enter which box:"))
        boardList[r - 1][c - 1] = "O"
        drawBoard()
        limitCounter = limitCounter + 1
    else:
        break
    if limitCounter < limit:
        print("player 2")
        r = int(input("enter which row:"))
        c = int(input("enter which box:"))
        boardList[r - 1][c - 1] = "X"
        drawBoard()
        limitCounter = limitCounter + 1
    else:
        break
