def nonDivisibleSubset(k, S):
    remainder_count = [0] * k

    # Count the frequency of each remainder
    for num in S:
        remainder_count[num % k] += 1

    # Start with at most one element divisible by k
    count = min(remainder_count[0], 1)

    # Loop through 1 to k//2 and select the max from remainder i and k-i
    for i in range(1, (k // 2) + 1):
        if i == k - i:
            # Only one can be chosen if k is even and remainder is k/2
            count += 1
        else:
            count += max(remainder_count[i], remainder_count[k - i])

    return count

