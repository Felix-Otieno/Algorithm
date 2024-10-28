unsortedData = [20, 33, 12, 53, 24, 65, 23, 4, 53, 1]
end = len(unsortedData)

def bubbleSort(data):
    global end
    for _ in range(0, end):
        for i in range(0, end):
            if i+1 < end:
                if data[i] > data[i+1]:
                    tempValue = data[i]
                    data[i] = data[i+1]
                    data[i+1] = tempValue
    end = end - 1
    return data

sortedData = bubbleSort(unsortedData)
print(sortedData)
