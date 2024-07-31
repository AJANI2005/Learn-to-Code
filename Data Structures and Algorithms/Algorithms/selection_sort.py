


def selection_sort(arr : list):
    sorted = []
    unsorted = arr.copy()
    while(len(unsorted)):
        smallest = unsorted[0]
        for n in unsorted:
            if n < smallest:
                smallest = n
        sorted.append(smallest)
        unsorted.remove(smallest)
    return sorted

array = [2,3,4,1,2,6,7]
print(selection_sort(array))
