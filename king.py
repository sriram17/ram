n,k=map(int,input().split())
a=list(map(int,input().split()))
b=a[::]
count=0
for i in range(0,n):
    b.remove(b[i])
    for j in b:
        sum=j+a[i]
        if sum==k:
            count=count+1
    b=a[::]
if(count==0):
    print("NO")
else:
    print("YES")
            
