def selectionS(arr, n):

    for i in range(n-1):
        mid_idx = i

        for j in range(i+1, n):
            if arr[mid_idx] > arr[j]:
                mid_idx = j

        arr[i], arr[mid_idx] = arr[mid_idx], arr[i]


# Time Complexity: O(n2) as there are two nested loops.
# Auxiliary Space: O(1)
# The good thing about selection sort is it never makes more than O(n) swaps
# and can be useful when memory write is a costly operation.


arr = [64, 25, 12, 22, 11]
n = 5

selectionS(arr, n)

print(arr)
