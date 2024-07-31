from math import floor

arr : int = [-2, 3, 4, 7, 8 , 9, 11, 13]
target = 1

low = 0
high = 7
mid = floor((low + high) / 2)


while True:
  
    if(arr[mid] == target):
        print("Found target at position: " + str(mid))
        break
    elif(high == low):
        print("Target not found")
        break
    else:
        if(arr[mid] > target):
            high = mid - 1
        else:
            low = mid + 1
        mid = floor((low + high) / 2)
        