a,b=map(int,input().split())
c=[]
for i in range(a+1,b):
  if(i%2==0):
    c.append(i)
print(*c)
