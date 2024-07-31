

nums = [2,3,1,6,5,8,4]
n = len(nums)

def swap(i,j,arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    
for i in range(n):
    for j in range(n - 1):
        if nums[j] > nums[j + 1]:
            swap(j,j + 1,nums)

print(nums)