#Ternary, compose of three parts
#Search, trying to find something by looking
#Ternary search, it is type of search algorithms that is designed to determine the position of the target value within a sorted array.
#Ternary search align with optimization problems. Ternary search is a search algorithm that can be used to find the minimum or maximum value of a function within a given interval.
#Divide the sorted array into three parts.

#Ternary Search is a search algorithm that works by dividing a sorted list into three equal parts. It then compares the target value with the middle element and the element two-thirds of the way through the list. Based on these comparisons, it eliminates two-thirds of the list and repeats the process until the target value is found or it's determined that the value doesn't exist.

def ternary_search(low, high, array, element):

    if low > high: 
        return "Element not found" 

    middle1 = low + (high - low) // 3
    middle2 = high - (high - low) // 3

    if array[middle1] == element:
        return f"Element found at index {middle1}"
    if array[middle2] == element:
        return f"Element found at index {middle2}"

    if element < array[middle1]:
        return ternary_search(low, middle1 - 1, array, element)
    elif element > array[middle2]:
        return ternary_search(middle2 + 1, high, array, element)
    else:
        return ternary_search(middle1 + 1, middle2 - 1, array, element)

array = [10, 20, 40, 60, 70, 90, 120, 150]
print(ternary_search(0, len(array) - 1, array, 60))
