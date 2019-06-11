N,Q=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(0,Q):
  u,v=map(int,input().split())
  b=a[u-1:v]
  for i in b:
    c=c^i
print(c)
