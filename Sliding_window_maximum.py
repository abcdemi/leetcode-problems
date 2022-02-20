import heapq as heapq
from math import inf

arr = [5,-3, 24, 0, -4,-3, 2, 112, 37]
k = 3

def sliding_max_naive(arr, k):
    window = []
    max_elem = - inf
    for j in range(k):
        window.append(arr[j])
        if arr[j] > max_elem:
            max_elem = arr[j]
    res = []
    res.append(max_elem)

    for i in range(k, len(arr)):
        window.append(arr[i])
        del window[0]
        max_elem = max(window)
        res.append(max_elem)
    
    return(res)
            

def sliding_max_heap(arr, k):
    if k == 1:
        return arr
    window = [(-val, i) for i, val in enumerate(arr[:k])]
    heapq.heapify(window)
    res = [-window[0][0]]

    for i in range(k, len(arr)):
        while window[0][1] <= i - k: 
            heapq.heappop(window)
        heapq.heappush(window, (-arr[i], i))
        res.append(-window[0][0])
        print(window, i)
    return res

def sliding_max_deque(arr, k):
    from collections import deque
    q = deque() # stores *indices*
    res = []
    for i, cur in enumerate(arr):
        while q and arr[q[-1]] <= cur:
            q.pop()
        q.append(i)
        # remove first element if it's outside the window
        if q[0] == i - k:
            q.popleft()
        # if window has k elements add to results
        #  first k-1 windows have < k elements
        #  because we start from empty window and add 1 element each iteration
        if i >= k - 1:
            res.append(arr[q[0]])
    return res

print(sliding_max_heap(arr, k))
print(sliding_max_deque(arr, k))
print(sliding_max_naive(arr, k))