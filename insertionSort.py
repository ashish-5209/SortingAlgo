Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
Algorithm
// Sort an arr[] of size n
insertionSort(arr, n)
Loop from i = 1 to n-1.
……a) Pick element arr[i] and insert it into sorted sequence arr[0…i-1]

def insertSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]

            j -= 1
        arr[j+1] = key

arr = [9,8,7,6,5,4,3,2,1]

insertSort(arr)
print(arr)
