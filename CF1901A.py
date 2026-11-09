t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = arr[0]
    
    for i in range(1, n):
        ans = max(ans, arr[i] - arr[i-1])
        
    ans = max(ans, 2 * (x - arr[-1]))
    
    print(ans)