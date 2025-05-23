def substrings(n):
    MOD = 10**9 + 7
    total = 0
    prev = 0

    for i in range(len(n)):
        digit = int(n[i])
        curr = (prev * 10 + digit * (i + 1)) % MOD
        total = (total + curr) % MOD
        prev = curr

    return total

# Input reading
n = input().strip()
print(substrings(n))
