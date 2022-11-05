import tkinter
from tkinter import messagebox

def Score(b, player, n):
    """
    :param b: given board as a 2D array
    :param l: S/O
    :param n: board size
    :return: boolean value for if l won a point that turn
    """
    score = 0
    if player == 'red':
        playerWin = "IndianRed1"
    else:
        playerWin = "SteelBlue1"
    overlap = "MediumPurple1"
    #check horizontal (rows) and vertical (columns)
    for i in range(n):
        temp = ''
        row = temp.join([b[i][j].cget('text') for j in range(n)]) #row as string
        col = temp.join([b[j][i].cget('text') for j in range(n)]) #col as string
        if row.__contains__("SOS"):
            SOSindices = [index for index in range(len(row)) if row.startswith('SOS', index)] #Get all instances  of SOS via their index in the row
            for r in SOSindices:
                colorRow = [b[i][r+k].cget("bg") for k in range(3)]
                if "Linen" in colorRow:
                    for g in range(len(colorRow)):
                        if b[i][r+g].cget("bg") == "Linen" :
                            b[i][r+g].config(bg=playerWin)
                        elif b[r + g][i].cget("bg") != playerWin and b[i][r+g].cget("bg") != "Linen":
                            b[i][r + g].config(bg=overlap)
                    score += 1
        if col.__contains__("SOS"):
            SOSindices = [index for index in range(len(col)) if col.startswith('SOS', index)] #Get all instances  of SOS via their index in the column
            for r in SOSindices:
                colorCol = [b[r+k][i].cget("bg") for k in range(3)]
                if "Linen" in colorCol:
                    for g in range(len(colorCol)):
                        if b[r+g][i].cget("bg") == "Linen":
                            b[r+g][i].config(bg=playerWin)
                        elif b[r+g][i].cget("bg") != playerWin and b[r+g][i].cget("bg") != "Linen":
                            b[r + g][i].config(bg=overlap)
                    score += 1

    #r to l diagnols
    m = 2
    d1 = 3
    while m < n:
        temp = ''
        buttons = []
        for i in range(d1):
            temp += b[m-i][i].cget('text')
            buttons.append(b[m-i][i])
        if temp.__contains__("SOS"):
            SOSindicesCol = [index for index in range(d1) if
                          temp.startswith('SOS', index)]  # Get all instances  of SOS via their index in the column
            SOSindicesRow = [m-index for index in range(d1) if
                          temp.startswith('SOS', index)]
            for cr in range(len(SOSindicesCol)):
                lmost = b[SOSindicesRow[cr]][SOSindicesCol[cr]]
                mid = b[SOSindicesRow[cr]-1][SOSindicesCol[cr]+1]
                rmost = b[SOSindicesRow[cr]-2][SOSindicesCol[cr]+2]
                diagTriplet = [lmost, mid, rmost]
                colorDiag = [button.cget("bg") for button in diagTriplet]
                if "Linen" in colorDiag:
                    for g in range(len(colorDiag)):
                        if diagTriplet[g].cget("bg") == "Linen":
                            diagTriplet[g].config(bg=playerWin)
                        elif diagTriplet[g].cget("bg") != playerWin and diagTriplet[g].cget("bg") != "Linen":
                            diagTriplet[g].config(bg=overlap)
                    score += 1
        d1 += 1
        m += 1

    #l to r diagnol
    d=0
    while (n+1)-d > 3:
        topTemp = ''
        bottomTemp = ''
        bottomButtons = []
        topButtons = []
        for i in range(0, n-d):
            rowNum = i
            colNum = i + d
            bottomButtons.append(b[rowNum][colNum])
            topButtons.append(b[colNum][rowNum])
            topTemp += b[rowNum][colNum].cget('text')
            bottomTemp += b[colNum][rowNum].cget('text')
        if topTemp.__contains__("SOS"):
            SOSindicesRow = [index for index in range(n-d) if
                          topTemp.startswith('SOS', index)]
            SOSindicesCol = [index+d for index in range(n-d) if
                          topTemp.startswith('SOS', index)]
            SOSIndices = list(zip(SOSindicesRow, SOSindicesCol))
            for SOSinstance in SOSIndices:
                lmost = b[SOSinstance[0]][SOSinstance[1]]
                mid = b[SOSinstance[0]+1][SOSinstance[1]+1]
                rmost = b[SOSinstance[0] + 2][SOSinstance[1] + 2]
                diagTriplet = [lmost, mid, rmost]
                colorDiag = [button.cget("bg") for button in diagTriplet]
                if "Linen" in colorDiag:
                    for g in range(len(colorDiag)):
                        if diagTriplet[g].cget("bg") == "Linen":
                            diagTriplet[g].config(bg=playerWin)
                        elif diagTriplet[g].cget("bg") != playerWin and diagTriplet[g].cget("bg") != "Linen":
                            diagTriplet[g].config(bg=overlap)
                    score += 1
        if bottomTemp.__contains__("SOS"):
            #print(bottomTemp)
            SOSindicesRow = [index+d for index in range(n-d) if
                          bottomTemp.startswith('SOS', index)]
            SOSindicesCol = [index for index in range(n-d) if
                          bottomTemp.startswith('SOS', index)]
            SOSIndices = list(zip(SOSindicesRow, SOSindicesCol))
            for SOSinstance in SOSIndices:
                lmost = b[SOSinstance[0]][SOSinstance[1]]
                mid = b[SOSinstance[0] + 1][SOSinstance[1] + 1]
                rmost = b[SOSinstance[0] + 2][SOSinstance[1] + 2]
                diagTriplet = [lmost, mid, rmost]
                colorDiag = [button.cget("bg") for button in diagTriplet]
                if "Linen" in colorDiag:
                    for g in range(len(colorDiag)):
                        if diagTriplet[g].cget("bg") == "Linen":
                            diagTriplet[g].config(bg=playerWin)
                        elif diagTriplet[g].cget("bg") != playerWin and diagTriplet[g].cget("bg") != "Linen":
                            diagTriplet[g].config(bg=overlap)
                    score += 1



        d += 1

    return score