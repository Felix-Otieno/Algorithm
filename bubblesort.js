const unsortedData = [20, 33, 12, 53, 24, 65, 23, 4, 53, 1];
let end = unsortedData.length - 1

const bubbleSort = (data) => {
    
    for (let i = 0; i < end; i++) {
        if (data[i] > data[i + 1]) {
            const valueInRight = data[i]
            data[i] = data[i+1]
            data[i+1] = valueInRight
        }
    }
    end--
}

for (let i = 0; i < unsortedData.length; i++) {
    bubbleSort(unsortedData)
}

console.log(unsortedData)