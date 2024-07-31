

nums : int = [1,3,2,5,4,6,7]

def swap(i,j,arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    
def partition(l,r,arr):
    pivot = r
    i = l - 1 # i is the index of the last number that should be on the left
    for j in range(l,r): #Exclude pivot index
        if arr[j] < arr[pivot]:
            i += 1
            swap(i,j,arr)
    swap(i+1,r,arr)
    return i+1   
     
def quick_sort(l,r,arr):
    #Base Case
    #A list cant be sorted if l >= r
    if l >= r: return
    #Split array into smaller than pivot and bigger than pivot
    p = partition(l,r,arr)
    quick_sort(l,p-1,arr)
    quick_sort(p+1,r,arr)

quick_sort(0,len(nums)-1,nums) 
print(nums)