import heapq

def largest_element(lst, K):
    heap = []
    for i in lst:
        if len(heap) < K:
            heapq.heappush(heap, i)
        else:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
    return heap[0]

# Call the function with a proper list and integer
print(largest_element([3, 2, 1, 5, 6, 7, 8, 9], 3))
