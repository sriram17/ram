n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
for i in a:
  if i not in c:
    c.append(i)
count=0
for j in c:
  for k in a:
    if j == k:
      count=count+1
  if count >1:
    d.append(j)
  count=0
print(*sorted(d))
