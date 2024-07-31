#Shifted Binary Search
from math import floor
from copy import deepcopy as copy




def wrap_around(n,min,max):
    if n > max:
        return min + (n - max - 1)
    if n < min:
        return max - (min - n - 1)
    return n




def shift(array, left = False):
    n = len(array)
    current_value_for_next = array[0]
    previous_value = 0
    if(left):
        for i in range(n,0,-1):
            next_idx = wrap_around(i-1,0,n-1)
            previous_value = array[next_idx]
            array[next_idx] = current_value_for_next
            current_value_for_next = previous_value
    else:
        for i in range(0,n,1):
            next_idx = wrap_around(i+1,0,n-1)
            previous_value = array[next_idx]
            array[next_idx] = current_value_for_next
            current_value_for_next = previous_value


def search(arr,target):
    n = len(arr)
    left = 0
    right = n - 1
    mid = floor((left + right) / 2)

    print(f"Binary Search: Target({target})", end="\n\n")
    while(right >= left):
       

        header : str = ""
        for i in range(n):
            lbl : str = ""
            if(i == left): lbl = "L"
            if(i == right): lbl = "R"
            if(i == mid): lbl = "M"

            header += str(lbl if lbl != "" else " ") + " "
        print(header)
        

        for i in range(n):        
            print(str(arr[i]) + " ",end="")
        print('\n')

        if(arr[mid] == target):
            print("Found target at position: " + str(mid))
            break

        if(target < arr[mid]):
            if(target >= arr[left]):
                right = mid - 1
            else:  left = mid + 1

        if(target > arr[mid]):
            if(target <= arr[right]):
                left = mid + 1
            else: right = mid - 1

        mid = floor((left + right) / 2)
            


        

        


            
        

  


arr = [5,6,7,8,9,1,2,3,4]
search(arr,4)

