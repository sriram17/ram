N,Q=map(int,input().split())
a=list(map(int,input().split()))
sum=0
for i in range(0,Q):
  u,v=map(int,input().split())
  b=a[u-1:v]
  for j in b:
    sum=sum+j
  print(sum)
  sum=0
