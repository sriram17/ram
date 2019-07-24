a=input()
a=list(a)
b=""
for i in range(0,len(a)):
    p=a.pop()
    b=b+p
if(a==b):
    print("YES")
else:
    print("NO")
    
