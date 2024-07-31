#Big O Notation

# T = O (1) + O (1) = C * 1 = O (1)
def func(array):
    total : int = 0 # O (1)
    return total # O (1)

# T = O (1) + O (1) + N * O (1)  + O (1) 
#   = O (1) + N * O (1) 
#   = N * C = O (N)

    
def sum(array):
    total : int = 0 # O (1)
    for i in array: # O (1)
        total += i # O (1)
    return total # O (1)