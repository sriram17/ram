a=input()
b=""
for i in range(len(a),-1,-1):
  b=b+a[i]
if(a==b):
  print("yes")
else:
  print("no")
