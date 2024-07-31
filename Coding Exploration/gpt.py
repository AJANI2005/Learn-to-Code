import curses
import math
import time

def draw_line(stdscr, x0, y0, x1, y1):
    """Draw a line between (x0, y0) and (x1, y1) using Bresenham's algorithm."""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < curses.COLS and 0 <= y0 < curses.LINES:
            stdscr.addch(y0, x0, '#')
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def draw_cube(stdscr, angle):
    stdscr.clear()
    rows, cols = stdscr.getmaxyx()
    
    # Cube vertices
    vertices = [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]
    
    # Rotation matrices around X, Y, Z axes
    rotation_x = [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]
    
    rotation_y = [
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ]
    
    rotation_z = [
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]
    
    # Apply rotations
    transformed_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        x, y, z = [
            sum(a*b for a, b in zip(row, [x, y, z]))
            for row in rotation_x
        ]
        x, y, z = [
            sum(a*b for a, b in zip(row, [x, y, z]))
            for row in rotation_y
        ]
        x, y, z = [
            sum(a*b for a, b in zip(row, [x, y, z]))
            for row in rotation_z
        ]
        transformed_vertices.append([x, y, z])
    
    # Project vertices onto 2D plane
    projected_vertices = [
        [int(cols / 2 + x * cols / 5 / (z + 2)), int(rows / 2 + y * rows / 5 / (z + 2))]
        for x, y, z in transformed_vertices
    ]
    
    # Edges of the cube
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]
    
    # Draw edges
    for edge in edges:
        start, end = edge
        start_x, start_y = projected_vertices[start]
        end_x, end_y = projected_vertices[end]
        draw_line(stdscr, start_x, start_y, end_x, end_y)
    
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    angle = 0
    while True:
        draw_cube(stdscr, angle)
        angle += 0.1
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
