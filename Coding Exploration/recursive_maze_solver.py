
maze = [
    "######################E##",
    "#..........#............#",
    "#.######.###.#####.###..#",
    "#.#....#.....#...#...#..#",
    "#.#.##.#####.#.#.###.#..#",
    "#.#.#.....#...#....######",
    "#.#.#.###.###############",
    "#.#.#.#.#.........#######",
    "#.#.#.#.#########.#######",
    "#.#.#.#.........#.#######",
    "#.#.###.#######.#.#######",
    "#.#.....#.....#.#.#######",
    "#.#######.###.#.#.#######",
    "#.........#.#.#.#.#######",
    "#########.#.#.#.#.#######",
    "#.........#.#.#.#.#######",
    "#.#########.###.#.#######",
    "#.#.............#.#######",
    "#.#.#############.#######",
    "#.#...............#######",
    "#.#######################",
    "#......................##",
    "######################.S#"
]
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def walk(maze : list[str],curr : Point,end : Point, wall : str, path : list[Point], seen: list[list[bool]]) -> bool:
    #Base Cases
   
    if(curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze)):
        return False
    if(maze[curr.y][curr.x] == wall):
        return False
    if(seen[curr.y][curr.x] == True):
        return False
    seen[curr.y][curr.x] = True

    path.append([curr.x,curr.y])
    if(curr.x == end.x and curr.y == end.y):
        return True
    
    
    
    
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    
   
    for n in dir:
        next = Point(curr.x + n[0],curr.y + n[1])
        if(walk(maze,next,end,wall,path,seen)):
            return True
           
    path.pop()        
    
    

def solve_maze(maze : list[str],start : str,end : str, wall : str) -> list[Point]:
    
    
    startPoint,endPoint = Point(0,0),Point(0,0)
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if(maze[y][x] == start) : startPoint = Point(x,y)
            if(maze[y][x] == end) : endPoint = Point(x,y)
        
    #Recursively Walk through maze
    seen = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = []
    walk(maze,startPoint,endPoint,wall,path,seen)
    
    #Trace Path
    if(len(path)):
        prev_x,prev_y = path[0][0],path[0][1]
        output = maze.copy()
        for p in path:
            x,y = p 

            sym = start
            if(prev_x == x and prev_y < y): sym = '↓'
            if(prev_x == x and prev_y > y): sym = '↑'    
            if(prev_y == y and prev_x < x): sym = '→'
            if(prev_y == y and prev_x > x): sym = '←'
            if(startPoint.y == y and startPoint.x == x) : sym = start 
            if(endPoint.y == y and endPoint.x == x) : sym = end           
                       
            output[y] = output[y][:x] + sym + output[y][x+1:]
            
            prev_x,prev_y = x,y    
        for y in output : print(y)   
                   
        
  
    return path



solve_maze(maze,"S","E","#")

