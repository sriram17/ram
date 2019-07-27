n=int(input())
a=list(map(int,input().split()))
b=a[::]
s=[]
pro=1
for i in range(0,n):
    b.remove(b[i])
    for j in b:
        pro=pro*j
    s.append(pro)
    pro=1
    b=a[::]
print(*s)
