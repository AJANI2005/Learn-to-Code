def swap(i,j,arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def insertion_sort(arr : list):
    unsorted = arr.copy()
    sorted = []
    while(len(unsorted)):
        value = unsorted.pop()
        sorted.append(value)
        if len(sorted) > 1:
            for i in range(len(sorted)-1,0,-1):
                if(sorted[i] < sorted[i-1]):
                    swap(i,i-1,sorted)
                else:
                    break
    return sorted
array = [5,2,3,4,6,10,1,16,33,22,10,12]
print(insertion_sort(array))          
            
        
        
