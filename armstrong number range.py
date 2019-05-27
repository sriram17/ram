a,b=input().split()
s=0
l=[]
for i in range(int(a)+1,int(b)):
  for j in str(i):
    s=s+int(j)**len(str(i))
  if(i==s):
    l.append(i)
  s=0
print(*l)
