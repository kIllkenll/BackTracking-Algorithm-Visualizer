
from turtle import pos
import pygame
import time
WIDTH = 550
background_color = (251,247,245)
current_color = (242, 58, 48)
original_grid_element_color = (52, 31, 151)
buffer = 5





def insertNum(win, num, position, grid, prev, first):
    pygame.font.init()
    i,j = position[0]+1, position[1]+1
    prevRow = prev[0]
    prevCol = prev[1]
    myfont = pygame.font.SysFont('Comic Sans MS',35)
    if position[0] != prevCol or position[1] != prevRow:
        if first == False:

            pygame.draw.rect(win, background_color, ((prevCol+1)*50 + buffer, (prevRow+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
            value = myfont.render(str(prev[2]), True, (0,0,0))
            win.blit(value, ((prevCol+1)*50 +15, (prevRow+1)*50))
        else:
            first = False
        # prevCol = position[0]
        # prevRow = position[1]
    

    grid[position[0]][position[1]] = num
    pygame.draw.rect(win, current_color, (j*50 + buffer, i*50+ buffer,50 -2*buffer , 50 - 2*buffer))
    
    value = myfont.render(str(num), True, (0,0,0))
    win.blit(value, (j*50 +15, i*50))
    pygame.display.update()
    return