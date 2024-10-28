unsortedData = [20, 33, 12, 53, 24, 65, 23, 4, 53, 1]
n = len(unsortedData)

def bubbleSort(data):
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break
    return data

sortedData = bubbleSort(unsortedData)
print(sortedData)