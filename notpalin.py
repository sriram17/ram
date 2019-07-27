a=input()
b=list(a)
i=0
c=""
while(i==0):
    if b==b[::-1]:
        b.pop()
        i=i+1
    else:
        i=i+1
for k in b:
    c=c+k
print(c)
    
