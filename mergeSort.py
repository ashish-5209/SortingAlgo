MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

def merge(arr,l, m, r):

    l1 = []
    l2 = []

    n1 = m-l + 1
    n2 = r - m

    for i in range(n1):
        l1.append(arr[l+i])
    for j in range(n2):
        l2.append(arr[m+1+j])

    x = 0
    y = 0
    k = l

    while x < n1 and y < n2:

        if l1[x] <= l2[y]:
            arr[k] = l1[x]
            x += 1
            k += 1
        else:
            arr[k] = l2[y]
            y += 1
            k += 1

    while x < n1:
        arr[k] = l1[x]
        x += 1
        k += 1

    while y < n2:
        arr[k] = l2[y]
        y += 1
        k += 1

def mergeSort(arr, l, r):

    if r > l:
        m = l + (r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr, 0, len(arr)-1)
    print("Sorted array is: ", end="\n")
    printList(arr)
