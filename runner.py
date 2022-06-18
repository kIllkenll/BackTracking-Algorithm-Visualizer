import pygame
import requests
from sudoku import solve
WIDTH = 550
background_color = (251,247,245)
original_grid_element_color = (52, 31, 151)
buffer = 5

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
win = pygame.display.set_mode((WIDTH, WIDTH))
def main():
    pygame.init()
    
    pygame.display.set_caption("Sudoku Back-Tracking Visualizor")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS',35)

    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()


    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()

    
    prev = [0,0,0]
    prev[2] = grid[0][0]
    # print(grid[0][0])
    runOnce = True
    firstRun = True
    while True: 
        if runOnce:
            s = solve(grid,win, prev,firstRun)
            if s:
                runOnce = False
                print(grid)
        for event in pygame.event.get(): 
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                return




def getBoard():
    return grid

main()