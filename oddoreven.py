a=int(input())
b=list(map(int,input().split()))
ans=[]
for i in range(0,len(b)):
    if i%2==0:
        if b[i]%2!=0:
            ans.append(b[i])
    else:
        if b[i]%2==0:
            ans.append(b[i])
print(*ans)
