def countingSort(s):
    arr = [""]*26

    for i in s:
        arr[ord(i)-ord('a')] += i


    return "".join(arr)

print(countingSort("geeksforgeeks"))

# Counting sort is efficient if the range of input data is not significantly
#greater than the number of objects to be sorted. Consider the situation where
# the input sequence is 
# between range 1 to 10K and the data is 10, 5, 10K, 5K.
