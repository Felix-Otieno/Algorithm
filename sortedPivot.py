#Rotated Sorted Array refers to a sorted array that has been shifted or rotated to the right or left by an unknown number of positions.



def binary_search(arr, low, high, x):
    # An iterative binary search function.
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def find_pivot(arr, low, high):
    # Function to get pivot. For array 3, 4, 5, 6, 1, 2 it returns 4 (index of 1) 
    while low < high:
        # The current subarray is already sorted, the minimum is at the low index
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        # The right half is not sorted. So the minimum element must be in the right half.
        if arr[mid] > arr[high]:
            low = mid + 1
        # The right half is sorted. Note that in this case, we do not change high to mid - 1
        # but keep it to mid. The mid element itself can be the smallest
        else:
            high = mid
    return low

def pivoted_binary_search(arr, n, key):
    #Searches an element key in a pivoted sorted array arr of size n 
    pivot = find_pivot(arr, 0, n - 1)

    # If the minimum element is present at index 0, then the whole array is sorted
    if pivot == 0:
        return binary_search(arr, 0, n - 1, key)

    # If we found a pivot, then first compare with pivot and then search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot

    if arr[0] <= key:
        return binary_search(arr, 0, pivot - 1, key)
    return binary_search(arr, pivot + 1, n - 1, key)

# Driver program to check above functions
if __name__ == "__main__":
    # Let us search 3 in below array
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    print(pivoted_binary_search(arr, len(arr), key))
