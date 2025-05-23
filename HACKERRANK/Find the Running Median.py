import heapq

def runningMedian(a):
    min_heap = []  # for larger half
    max_heap = []  # for smaller half (as negative numbers)
    medians = []

    for num in a:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # Balance the heaps
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Calculate median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = -max_heap[0] * 1.0

        medians.append(median)

    return medians

# Input reading
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

# Get result and print with 1 decimal place
medians = runningMedian(a)
for m in medians:
    print("{:.1f}".format(m))
