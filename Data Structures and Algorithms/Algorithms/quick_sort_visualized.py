# Example file showing a basic pygame "game loop"
import pygame,random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


x_values = []
h_values = []

n = 200
w = screen.get_width() / n

for i in range(n):
    x_values.append(i * w)
    h_values.append(random.uniform(0,screen.get_height()))




def swap(i,j,arr):

    swapped : bool = False
    x1 : float = x_values[i]
    x2 : float = x_values[j]


    while(not swapped):
      
        #Swap Animation (X values)
        d1 = (x1 - x_values[i])
        d2 = (x2 - x_values[j])
        x_values[i] += d1 * 0.01
        x_values[j] += d2 * 0.01

        if(abs(d1) < 1) : x_values[i] = x1
        if(abs(d2) < 1) : x_values[j] = x2

        if(x_values[i] == x1 and x_values[j] == x2):
            swapped = True
            #Perform Value Swap
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp   
        run()
        
 
    
       


def partition(arr,l,r):
    pivot = arr[r]
    i = l - 1
    for j in range(l,r):
        if arr[j] < pivot:
            i += 1
            swap(i,j,arr)
    swap(i+1,r,arr)    
    return i+1


def quicksort(arr,l,r):
    if(l >= r):
        return
    p = partition(arr,l,r)
    quicksort(arr,l,p - 1)
    quicksort(arr,p + 1,r)

def input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            pygame.quit()
def render():
    screen.fill("black")
    for i in range(n):
        pygame.draw.rect(screen,"white",(x_values[i],screen.get_height() - h_values[i], w/2, h_values[i]))
    pygame.display.flip()

def update():
    clock.tick(144)
    

def run():
    input()
    render()
    update()

while running:
    
    quicksort(h_values,0,n-1)
    run()
   

pygame.quit()