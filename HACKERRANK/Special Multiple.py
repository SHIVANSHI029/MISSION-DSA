from collections import deque

def find_smallest_multiple(n):
    visited = set()
    q = deque()
    
    q.append(("9", 9 % n))
    visited.add(9 % n)
    
    while q:
        num_str, rem = q.popleft()
        
        if rem == 0:
            return num_str
        
        # Try appending '0'
        rem0 = (rem * 10) % n
        if rem0 not in visited:
            q.append((num_str + "0", rem0))
            visited.add(rem0)
        
        # Try appending '9'
        rem9 = (rem * 10 + 9) % n
        if rem9 not in visited:
            q.append((num_str + "9", rem9))
            visited.add(rem9)

# Main input/output
T = int(input())
for _ in range(T):
    N = int(input())
    print(find_smallest_multiple(N))
