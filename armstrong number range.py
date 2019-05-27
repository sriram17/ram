a,b=input().split()
c=0
l=[]
for i in range(int(a+1),int(b)):
  for j in str(i):
    c=c+int(j)**len(i)
  if(i==c):
    l.apprnd(i)
  c=0
print(*l)
