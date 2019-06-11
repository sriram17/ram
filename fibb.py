N=int(input())
a=list(map(int,input().split()))
b=0
c=0
for i in a:
  b=i-b
  c=c+b
print(c)
