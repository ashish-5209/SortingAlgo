def partition(arr, l, h):
    i = l
    j = h
    pivot = arr[l]

    while True:
        while arr[i] < pivot:
            i +=1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quickS(arr, l, h):

    if l < h:
        p = partition(arr, l, h)
        quickS(arr, l, p)
        quickS(arr, p+1, h)


arr = [12, 11, 13, 5, 6, 7, 1]
quickS(arr, 0, 6)
print(arr)
