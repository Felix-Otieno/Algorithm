def rotatedArrSearch(rotatedArr, num):
    leftIdx = 0
    rightIdx = len(rotatedArr) - 1

    # Edge case: if the array is empty
    if len(rotatedArr) == 0:
        return -1

    # Find the pivot where the rotation happens
    while leftIdx < rightIdx:
        mid = (rightIdx + leftIdx) // 2
        if rotatedArr[mid] > rotatedArr[rightIdx]:
            leftIdx = mid + 1
        else:
            rightIdx = mid

    pivot = leftIdx
    leftIdx = 0
    rightIdx = len(rotatedArr) - 1

    # Determine which part of the array to search in
    if num >= rotatedArr[pivot] and num <= rotatedArr[rightIdx]:
        leftIdx = pivot  # Search the right part
    else:
        rightIdx = pivot - 1  # Search the left part

    # Perform binary search
    while leftIdx <= rightIdx:
        mid = (rightIdx + leftIdx) // 2
        if rotatedArr[mid] == num:
            return mid
        elif num > rotatedArr[mid]:
            leftIdx = mid + 1
        else:
            rightIdx = mid - 1

    return -1  # Return -1 if not found

rotatedArr = [0,3,6,9,12,15,18,21,24,27,30]
num = 21
print(rotatedArrSearch(rotatedArr, num))  # This should output 4
