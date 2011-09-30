import random

arr = [ random.randint(0, 100) for i in range(0, 10) ]

print "Initial array is:", arr

def mergesort(arr):
    def domergesort(arr1, arr2):
        """
        Actual implementation of merge sort
        """
        if len(arr1) > 1:
            marr1 = domergesort(arr1[:len(arr1)/2], arr1[len(arr1)/2:])
        else:
            marr1 = arr1
        if len(arr2) > 1:
            marr2 = domergesort(arr2[:len(arr2)/2], arr2[len(arr2)/2:])
        else:
            marr2 = arr2

        # now both arrays are sorted, merge them
        arr1index = 0
        arr2index = 0
        marr = []
        while (arr1index < len(marr1)) or (arr2index < len(marr2)):
            # array 1 fully merged take element from array 2
            if arr1index == len(marr1):
                marr.append(marr2[arr2index])
                arr2index = arr2index + 1
            # array 2 fully merged take element from array 1
            elif arr2index == len(marr2):
                marr.append(marr1[arr1index])
                arr1index = arr1index + 1
            # both arrays still have elements but array 1 elem <= array 2 elem
            elif marr1[arr1index] <= marr2[arr2index]:
                marr.append(marr1[arr1index])
                arr1index = arr1index + 1
            # both arrays still have elements but array 1 elem > array 2 elem
            elif marr1[arr1index] > marr2[arr2index]:
                marr.append(marr2[arr2index])
                arr2index = arr2index + 1
             
        return marr
    
    if len(arr) <= 1:
        return arr
    else:
        return domergesort(arr[:len(arr)/2], arr[len(arr)/2:])
    
print "Merged array is:", mergesort(arr)