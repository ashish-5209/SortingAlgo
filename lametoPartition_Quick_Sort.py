def quickS(arr, l, h):

    if l < h:

        p = partition(arr, l, h)
        quickS(arr, l, p-1)
        quickS(arr, p+1, h)

def partition(arr, l, h):

    pivot = arr[h]
    i = l-1
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return (i+1)


arr = [12, 11, 13, 5, 6, 7]
quickS(arr, 0, 5)
print(arr)
