# Python Program to search a specific element in the sorted array, which is rotated at a pivot  
    
# Defining the function to search the element target in the pivoted array.   
# The function will first find the pivot and then perform a binary search  
def pivotedSearch(array, n, target):  
  
    # Find the pivot of the array  
    pivot = findPivot(array, 0, n - 1);  
    print("The pivot of the array is: ", pivot)  
    # If there is no pivot in the array, that means the array is not rotated  
    if pivot == -1:  
        # Apply binary search on the complete array  
        return binarySearch(array, 0, n - 1, target);  
    
    # If we could find a pivot, then firstly, we will compare the pivot element with the target element  
    if array[pivot] == target:  
        return pivot  
    # Else, compare the 0th element of the original array to the target  
    elif array[0] <= target:  
        # Search in the left sub-array  
        return binarySearch(array, 0, pivot - 1, target)  
    else:  
        # Search in the right sub-array  
        return binarySearch(array, pivot + 1, n - 1, target)  
    
    
# Defining a function to find the pivot of the array   
# For an array [4, 5, 6, 7, 1, 2, 3], it will return 3   
# (index of 7)   
def findPivot(array, l, h):  
        
    # base cases of the recursive function  
    if h < l:  
        return -1  
    if h == l:  
        return l  
      
    # [l + (h - l)/2]. This is same as [(l + h)/2]. We use the prior one to avoid overflow condition  
    mid = l + ((h - l) // 2)  
      
    if mid < h and array[mid] > array[mid + 1]:  
        return mid  
    if mid > l and array[mid] < array[mid - 1]:  
        return (mid - 1)  
    if array[l] >= array[mid]:  
        return findPivot(array, l, mid - 1)  
    return findPivot(array, mid + 1, h)  
    
# Defining the function to perform a standard binary search  
def binarySearch(array, l, h, target):  
    
    if h < l:  
        return -1  
            
    # l + (h - l)/2     
    mid = l + ((h - l) // 2)  
        
    if target == array[mid]:  
        return mid  
    if target > array[mid]:  
        return binarySearch(array, (mid + 1), h, target)  
    return binarySearch(array, l, (mid - 1), target)  
    
    
# Calling the function and passing the array and target element to it  
# We will search 2 in the below array  
array = [4, 5, 6, 7, 1, 2, 3]  
n = len(array)  
target = 2  
print(f"The index of {target} in the {array} array is: ", pivotedSearch(array, n, target))  