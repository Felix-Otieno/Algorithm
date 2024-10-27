def find_kth_largest(nums, K):
    """
    A function that finds the Kth largest element in the unsorted list and takes two parameters: 
    """
    # Sort the list in descending order
    sorted_nums = sorted(nums, reverse=True)
    
    # Return the element at index k-1
    return sorted_nums[k-1]
nums = [45, 20, 97, 15, 70, 69, 32, 88, 45]
k = 1

kth_largest = find_kth_largest(nums, K)
print(f"The {k}th largest element is: {kth_largest}")