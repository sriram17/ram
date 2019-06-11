a=list(map(int,input().split()))
a=sorted(a)
b=[]
s=0
count=0
for i in a:
    if i not in b:
        b.append(i)
for j in range(0,len(b)):
    for k in range(0,len(a)):
        if(b[j]==a[k]):
            count=count+1
    s=s+((j+1)*count)
    count=0
print(s)
        
    
