a=input()
c=list(a)
b=""
for i in range(0,len(c)):
    p=c.pop()
    b=b+p
if(a==b):
    print("YES")
else:
    print("NO")
    
