def swap(i, j, arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def heapify(arr, n, i, reverse):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    if reverse:
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
    else:
        if left < n and arr[largest] > arr[left]:
            largest = left
        if right < n and arr[largest] > arr[right]:
            largest = right

    if largest != i:
        swap(i, largest, arr)
        heapify(arr, n, largest, reverse)

def build_heap(arr, reverse):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, reverse)

def heap_sort(array, reverse=False):
    result = array.copy()
    n = len(result)

    build_heap(result, reverse)

    for i in range(n - 1, 0, -1):
        swap(0, i, result)
        heapify(result, i, 0, reverse)

    return result

nums = [2, 3, 1, 6, 5, 8, 4]
print(heap_sort(nums, False))  # Ascending order
print(heap_sort(nums, True))   # Descending order
