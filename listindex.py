n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(0,len(a)):
  if(a[i]==i):
    c.append(a[i])
print(*sorted(c))
