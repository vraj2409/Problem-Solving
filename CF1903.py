t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    if k >= 2 or arr == sorted(arr):
        print("YES")
    else:
        print("NO")