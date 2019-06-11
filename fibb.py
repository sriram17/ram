N=int(input())
a=list(map(int,input().split()))
b=0
c=0
for i in range(0,len(a)):
  if(i==0):
    c=a[i]-c
  else:
    c=c+(a[i]-a[0])
print(c)
