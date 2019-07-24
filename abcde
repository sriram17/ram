s=int(input())
a=list(map(int,input().split()))
c=[]
count=0
ct=0
for i in a:
  if i not in c:
    c.append(i)
for j in c:
  for k in a:
    if j==k:
      count=count+1
  if count>1:
    ct=ct+1
  count=0
if ct=0:
  print("unique")
else:
  print(ct)
