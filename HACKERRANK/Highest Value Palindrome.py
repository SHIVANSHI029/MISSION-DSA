def highestValuePalindrome(s, n, k):
    s = list(s)
    changes = [0] * n  # To track which positions were changed
    l, r = 0, n - 1

    # First pass: make it a palindrome
    while l < r:
        if s[l] != s[r]:
            # Change the smaller one to the larger one
            bigger = max(s[l], s[r])
            s[l] = s[r] = bigger
            changes[l] = changes[r] = 1
            k -= 1
        l += 1
        r -= 1

    if k < 0:
        return "-1"

    # Second pass: maximize value by turning digits to '9'
    l, r = 0, n - 1
    while l <= r:
        if l == r:
            # Middle digit in odd-length string
            if k > 0 and s[l] != '9':
                s[l] = '9'
                k -= 1
        elif s[l] != '9':
            # Check if we can change both to 9
            if k >= 2 - changes[l] - changes[r]:
                s[l] = s[r] = '9'
                k -= 2 - changes[l] - changes[r]
        l += 1
        r -= 1

    return ''.join(s)
