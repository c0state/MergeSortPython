def mergesort(array):
    if len(array) < 2:
        return array
    else:
        subarray1 = mergesort(array[:len(array)/2])
        subarray2 = mergesort(array[len(array)/2:])
    
    # merge sorted sub-arrays
    arr1index = 0
    arr2index = 0
    mergedarray = []
    while (arr1index < len(subarray1)) or (arr2index < len(subarray2)):
        # array 1 fully merged take element from array 2
        if arr1index == len(subarray1):
            mergedarray.append(subarray2[arr2index])
            arr2index = arr2index + 1
        # array 2 fully merged take element from array 1
        elif arr2index == len(subarray2):
            mergedarray.append(subarray1[arr1index])
            arr1index = arr1index + 1
        # both arrays still have elements but array 1 elem <= array 2 elem
        elif subarray1[arr1index] <= subarray2[arr2index]:
            mergedarray.append(subarray1[arr1index])
            arr1index = arr1index + 1
        # both arrays still have elements but array 1 elem > array 2 elem
        elif subarray1[arr1index] > subarray2[arr2index]:
            mergedarray.append(subarray2[arr2index])
            arr2index = arr2index + 1
         
    return mergedarray
    
if __name__ == "__main__":
    import random
    
    array = [ random.randint(0, 100) for i in range(0, 10) ]
    
    print "Initial array is:", array
    print "Merged array is:", mergesort(array)