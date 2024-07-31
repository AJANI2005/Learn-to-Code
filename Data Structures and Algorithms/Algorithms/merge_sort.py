
def merge(leftArray,rightArray):
    i = 0
    j = 0
    result = []
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            result.append(leftArray[i])
            i+=1
        else:
            result.append(rightArray[j])
            j+=1
        
        
        
    while i < len(leftArray):
        result.append(leftArray[i])
        i+=1
            
    while j < len(rightArray):
        result.append(rightArray[j])
        j+=1    
        
        
    return result

def merge_sort(arr):
    if(len(arr) == 1) : return arr
    
    pivot = len(arr) // 2
    left = arr[:pivot]
    right = arr[pivot:]
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)
    
print(merge_sort([1,10,15,4,5,6]))