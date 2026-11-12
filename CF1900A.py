t = int(input())

for _ in range(t):
    n = int(input())
    str = input()
    l = list(str)
    print(str,l)

    ans = 0
    for i in range(1,n-1):
        print(l[i])
        if l[i] == '#':
            continue
        if l[i] == '.' : 
            if l[i-1] == '.' and l[i+1] == '.':
                ans += 2
                l[i] = l[i+1] = l[i-1] = 'w'
            elif i > 1 and l[i-2] == 'w' and l[i-1] == 'w':
                l[i] = 'w'
            elif l[i-1] == '.':
                ans += 2
                l[i] = l[i-1] = 'w'
            else:
                ans += 1
                l[i] = 'w'
        else:
            if l[i] == 'w':
                if l[i+1] == '.' and l[i-1] == 'w':
                    l[i+1] = 'w'
    print(ans)