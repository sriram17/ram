N,Q=map(int,input().split())
a=list(map(int,input().split()))
for i in range(0,Q):
  u,v=map(int,input().split())
  b=a[u-1:v]
  print(min(b))
