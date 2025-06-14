# Number of test cases
t = int(input())

for _ in range(t):
    # Read size of set A (not needed directly)
    len_a = int(input())
    a = set(input().split())
    
    # Read size of set B (not needed directly)
    len_b = int(input())
    b = set(input().split())
    
    # Check if A is a subset of B
    print(a.issubset(b))
