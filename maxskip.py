n=int(input())
a=list(map(int,input().split()))
c=[]
pro=1
for i in range(n):
    b=a[i:]
    for j in b:
        pro=pro*j
        c.append(pro)
    pro=1
print(max(c))
