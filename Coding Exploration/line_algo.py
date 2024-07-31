import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_COLOR = (200, 200, 200)
BG_COLOR = (0, 0, 0)
START_COLOR = (0, 255, 0)
END_COLOR = (0, 0, 255)
LINE_COLOR = (255, 0, 0)
DEFAULT_COLOR = BG_COLOR

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Grid with Movable Line Endpoints")

# Initial start and end points
start_pos = (20, 20)
end_pos = (15, 10)
dragging_start = False
dragging_end = False

# Create a 2D array to represent the grid
rows = HEIGHT // CELL_SIZE
cols = WIDTH // CELL_SIZE
grid = [[DEFAULT_COLOR for _ in range(cols)] for _ in range(rows)]

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

def draw_cells():
    for row in range(rows):
        for col in range(cols):
            color = grid[row][col]
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

def draw_line():
    start_pixel = (start_pos[0] * CELL_SIZE + CELL_SIZE // 2, start_pos[1] * CELL_SIZE + CELL_SIZE // 2)
    end_pixel = (end_pos[0] * CELL_SIZE + CELL_SIZE // 2, end_pos[1] * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.line(screen, LINE_COLOR, start_pixel, end_pixel, 3)

def draw_points():
    start_pixel = (start_pos[0] * CELL_SIZE + CELL_SIZE // 2, start_pos[1] * CELL_SIZE + CELL_SIZE // 2)
    end_pixel = (end_pos[0] * CELL_SIZE + CELL_SIZE // 2, end_pos[1] * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(screen, START_COLOR, start_pixel, CELL_SIZE // 3)
    pygame.draw.circle(screen, END_COLOR, end_pixel, CELL_SIZE // 3)


def line_algo():
    x0, y0 = start_pos
    x1, y1 = end_pos

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    xstep = 1 if x0 < x1 else -1
    ystep = 1 if y0 < y1 else -1
    
    if dx > dy:
        d = 2 * dy - dx
        y = y0
        for x in range(x0, x1 + xstep, xstep):
            if x >= 0 and x < cols and y >= 0 and y < rows:
                grid[y][x] = "blue"
            if d > 0:
                y += ystep
                d -= 2 * dx
            d += 2 * dy
    else:
        d = 2 * dx - dy
        x = x0
        for y in range(y0, y1 + ystep, ystep):
            if x >= 0 and x < cols and y >= 0 and y < rows:
                grid[y][x] = "blue"
            if d > 0:
                x += xstep
                d -= 2 * dy
            d += 2 * dx

        
      
        
                
     
        
            
       
       
    
        
def reset_cells():
    for y in range(rows):
        for x in range(cols):
            grid[y][x] = "black"
 

# Main loop
running = True
while running:
    screen.fill(BG_COLOR)
    line_algo()
    draw_cells()
    reset_cells()
    draw_grid()
    draw_line()
    draw_points()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
            if (grid_x, grid_y) == start_pos:
                dragging_start = True
            elif (grid_x, grid_y) == end_pos:
                dragging_end = True
            else:
                grid[grid_y][grid_x] = (255, 255, 0)  # Change the color of the clicked cell
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_start = False
            dragging_end = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging_start:
                x, y = event.pos
                start_pos = (x // CELL_SIZE, y // CELL_SIZE)
            elif dragging_end:
                x, y = event.pos
                end_pos = (x // CELL_SIZE, y // CELL_SIZE)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
