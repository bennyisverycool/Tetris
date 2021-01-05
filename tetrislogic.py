import random
import pygame
from Piece import *
col = 10
row = 20
screenWidth = 800
screenHeight = 750
gameWidth = 300
gameHeight = 600
blockSize = 30

top_left_x = (screenWidth - gameWidth) // 2
top_left_y = screenHeight - gameHeight

I = [[
        ".....",
        "0000.",
        ".....",
        ".....",
        "....."],
    [
        "..0..",
        "..0..",
        "..0..",
        "..0..",
        "....."]]
        
L = [[
        ".....",
        ".....",
        "0....",
        "0....",
        "00..."],
    [
        "..000",
        "..0..",
        ".....",
        ".....",
        "....."],
        [
        ".....",
        ".....",
        ".00..",
        "..0..",
        "..0.."],
        [
        "....0",
        "..000",
        ".....",
        ".....",
        "....."]
        ]

B = [[
        ".00..",
        ".00..",
        ".....",
        ".....",
        "....."
    ]]

T = [[
        ".000.",
        "..0..",
        ".....",
        ".....",
        "....."
    ],
    [
        "....0",
        "...00",
        "....0",
        ".....",
        "....."
    ],
    [
        "..0..",
        ".000.",
        ".....",
        ".....",
        "....."
    ],
    [
        "0....",
        "00...",
        "0....",
        ".....",
        "....."
    ]]
        
J = [['.....',
    '.0...',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..00.',
    '..0..',
    '..0..',
    '.....'],
    ['.....',
    '.....',
    '.000.',
    '...0.',
    '.....'],
    ['.....',
    '..0..',
    '..0..',
    '.00..',
    '.....']]


Z = [['.....',
    '.....',
    '.00..',
    '..00.',
    '.....'],
    ['.....',
    '..0..',
    '.00..',
    '.0...',
    '.....']]


shapes = [Z, B, L, T, I, J]

shapes_colors = [(255, 0, 0), (255, 255, 255), (255, 128, 0), (0,0,102),(255,255,0),(0,51,0)]

class Piece (object):
    rows = 20 
    col = 10 

    def __init__(self, col, row, shape):
        self. x= col 
        self.y = row 
        self.shape = shape 
        self.shapes_color = shapes_colors[shapes.index(shape)]
        self.rotation = 0 
        # rotation foes from 0 to 3 



def create_grid(locked_position = {}):
    grid = []
    for x in range(20):
        lst = []
        for i in range(10):
            lst.append((0,0,0))
        grid.append(lst)


def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False 
    return True

def draw_grid(surface, row , col):
    sx = top_left_x
    sy = top_left_y

    for i in range(row):
        # horizontal
        pygame.draw.line(surface, (0,0,0), (sx,  sy + i * 30), (sx + gameWidth, sy + i * 30)) 
        for j in range(col):
            # vertical 
            pygame.draw.line(surface, (0,0,0), (sx + j * 30, sy), (sx + j * 30, sy + gameHeight))  

            
def get_shape():
    global shape
    global shape_color
    return Piece(5,0,random.choice(shapes))

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]



    for i , line in enumerate(format):
        row - list(line)
        for j, col in enumerate(row):
            if col == "0": 
                positions.append((shape.x + j, shape.y + i))

    
    for i , pos in  enumerate(positions):
        positions[i] = (pos[0] - 1, pos[1] - 4)

    return positions



def main():
    global grid
    locked_positions= {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True 
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock
    falltime = 0
    leveltime = 0
    fallspeed = 0.27
    score = 0
    while run:
        grid = create_grid(locked_position)
        falltime+=clock.get_rawtime()
        leveltime +=clock.get_rawtime()
        clock.tick()
        if(leveltime / 1000 > 4):
            leveltime = 0
            if(fallspeed > .15):
                fallspeed -=0.0005
        if falltime / 1000 >= fallspeed:
            falltime = 0
            current_piece.y +=1
            change_piece = True

            
        for event in pygame.event.get():


                        
            if event.type == pygame.QUIT:      #if user wants to quit
                run = False                     #stop while loop
                pygame.quit()                  #quit/exit pygame



            # if the type of my event relates to keyboard stuff
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT  or pygame.K_A: # if user presses a or left arrow key
                    current_piece.x -= 1                      #  move left
                    if not valid_space(current_piece,grid):  # if after the piece moves left, it is not in a valid space, undo all actions.
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT or pygame.K_D:  # if user presses d or right arrow key 
                    current_piece.x +=1                        #moves right
                    if not valid_space(current_piece,grid):
                        current_piece.x -= 1                        # if after the piece moves right, it is not in a valid space, undo all actions by reversing it.
                if event.key == pygame.K_UP or pygame.K_W:      # if user presses either w or up arrow
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)         # rotate piece       
                    if not valid_space(current_piece,grid):                                                  
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)   
                if event.key == pygame.K_DOWN or pygame.K_S:
                    current_piece.y += 1      
                    if not valid_space(current_piece,grid):
                        current_piece.y -= 1    
        shape_pos = convert_shape_format(current_piece)


        for i in range(len(shape_pos)):
            x,y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
                
        if change_piece:
            for pos in shape_pos:
               p = (pos[0], pos[1])
               locked_positions[p] = current_piece.color 


        # This function is still not done


    
def main_menu():
    run = True

    while run:
        win.fill((0,0,0))
        draw_text_middle("Press any key ro begin.", 60, (255,255,255), win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:     
                run = False                     
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                main()
            
#start main menu
#comment main func code
