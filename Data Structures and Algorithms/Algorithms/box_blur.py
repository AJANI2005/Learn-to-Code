# Example file showing a basic pygame "game loop"
import pygame
import pygame_widgets
from pygame_widgets.button import Button




import math
import random 
import copy
from pprint import pprint
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


cellSize = pygame.Vector2(32,32)
gridSize = pygame.Vector2(screen.get_width()/cellSize.x,screen.get_height()/cellSize.y)
button =  Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    100,  # X-coordinate of top left corner
    100,  # Y-coordinate of top left corner
    100,  # Width
    50,  # Height

    # Optional Parameters
    text='Add Blur',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(10,10,10),  # Colour of button when not being interacted with
    hoverColour=(50,50,50),  # Colour of button when being hovered over
    pressedColour=(100,100,100),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    textColour =(255,255,255)
    
)


class Node:
    def __init__(self,x,y,color):
        self.x,self.y = x,y
        self.color = color
    def draw(self):
        sizeX = cellSize.x
        sizeY = cellSize.y 
        pygame.draw.rect(screen,self.color,(node.x - sizeX/2,node.y - sizeX/2,sizeX,sizeY))



grid = [] 
def CreateGrid() -> None: 
    for x in range(0, int(gridSize.x)):
        newArray = []
        for y in range(0, int(gridSize.y)):
            c : int = random.randint(0,255)
            randomColor : pygame.Color = pygame.Color(
                c,0,random.randint(0,255))
            
            x_pos : float = x * cellSize.x + cellSize.x/2
            y_pos : float = y * cellSize.y + cellSize.y/2

            newArray.append(Node(x_pos,y_pos,randomColor))
        grid.append(newArray)


def BlurGrid(amt : int = 3) -> None: 
    global grid

    kernelSize : int = int((amt - 1) / 2)


    newGrid = copy.deepcopy(grid)
    for x in range(0, int(gridSize.x)):
        for y in range(0, int(gridSize.y)):
            sum : pygame.Vector3 = pygame.Vector3(0,0,0)
            for i in range(-kernelSize,kernelSize + 1):
                for j in range(-kernelSize,kernelSize + 1):
                    checkX = int(pygame.math.clamp(x + i,0,gridSize.x - 1))
                    checkY = int(pygame.math.clamp(y + j,0,gridSize.y - 1))
                    node : Node = grid[checkX][checkY]
                    sum.x += node.color.r
                    sum.y += node.color.g
                    sum.z += node.color.b
                    
                    
            sum /= (amt * amt) 
            newGrid[x][y].color = pygame.Color(int(sum.x),int(sum.y),int(sum.z))
    grid = copy.deepcopy(newGrid)      




CreateGrid()

while running:
    # poll for events
    events = pygame.event.get()
    # pygame.QUIT event means the user clicked X to close your window
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #Draw Cells
    button.onClick = lambda: BlurGrid(3)

     
    for x in range(0, int(gridSize.x)):
        for y in range(0, int(gridSize.y)):
            node : Node = grid[x][y]
            node.draw()
            
     
    
    pygame_widgets.update(events)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()