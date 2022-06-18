
from numpy import insert
# from runner import insertNum, getBoard
from functions import insertNum
import time
# board = getBoard()

pauseTime = 0.1

def solve(bo, win, prev,firstRun):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find


    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            insertNum(win, i, (row, col), bo, prev, firstRun)
            firstRun = False
            prev[0] = row
            prev[1] = col
            prev[2] = i
            time.sleep(pauseTime)
            if solve(bo, win, prev,firstRun):
                return True
            
            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i,j)

    return None


    


#print_board(board)

# solve(board)
# print("__________________")
# print_board(board)
