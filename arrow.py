a=list(map(int,input().split()))
b=a[::-1]
c=""
for i in range(0,len(b)):
    if i==len(b)-1:
        c=c+str(b[i])
    else:
        c=c+str(b[i])+"->"
print(c)
