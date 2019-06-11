n=int(input())
a=list(map(int,input().split()))
b=sorted(a)[::-1]
c=""
if(a==[0]*n):
    print("0")
else:
    for i in b:
        c=c+str(i)
    print(int(c))    
