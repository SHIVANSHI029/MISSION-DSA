from collections import defaultdict

def count_divisible_subsequences(n, k, arr):
    mod_count = defaultdict(int)
    mod_count[0] = 1
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num
        mod = prefix_sum % k
        mod = (mod + k) % k  # handle negative mod
        count += mod_count[mod]
        mod_count[mod] += 1

    return count

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_divisible_subsequences(n, k, arr))
