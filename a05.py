N,K = map(int,input().split())
ans = 0 
for i in range(1,N+1):
    for j in range(1,N+1):
        tmp = i+j
        if tmp>=K:
            continue
        else:
            k = K - tmp
            if k <= N:
                ans += 1
print(ans)
