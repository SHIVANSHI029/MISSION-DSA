def fairRations(B):
    n = len(B)
    loaves_distributed = 0
    
    # Check the count of odd numbers
    odd_count = sum(1 for x in B if x % 2 != 0)
    
    # If odd count is odd, impossible to make all even
    if odd_count % 2 != 0:
        return "NO"
    
    # Iterate over the list to fix odd counts
    for i in range(n - 1):
        if B[i] % 2 != 0:
            # Give a loaf to current person and the next person
            B[i] += 1
            B[i + 1] += 1
            loaves_distributed += 2
    
    return str(loaves_distributed)
