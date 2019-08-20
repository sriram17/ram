a=input()
b=list(a)
c=b[::]
f=0
for i in range(0,len(b)):
 c.remove(b[i])
 if c==c[::-1]:
  f=f+1
 c=b[::]
if f>0:
 print("YES")
else:
 print("NO")
