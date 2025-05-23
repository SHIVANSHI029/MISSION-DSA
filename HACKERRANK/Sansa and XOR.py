def sansaXor(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        if ((i + 1) * (n - i)) % 2 == 1:
            result ^= arr[i]
    return result

# Input reading
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sansaXor(arr))
