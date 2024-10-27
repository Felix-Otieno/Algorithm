def pivoted_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Case 1: Find key
        if arr[mid] == key:
            return mid

        # Case 2: Left half is sorted
        if arr[mid] >= arr[low]:
            if key >= arr[low] and key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Case 3: Right half is sorted
        else:
            if key > arr[mid] and key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1  # Key not found

# Driver code
arr1 = [35, 45, 55, 65, 75, 5, 10, 15, 25]
key1 = 0
result1 = pivoted_search(arr1, key1)
print(result1)  # Output: 4

arr2 = [4, 5, 6, 7, 0, 1, 2]
key2 = 3
result2 = pivoted_search(arr2, key2)
print(result2)  # Output: -1