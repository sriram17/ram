a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
h=[]
for i in c:
    if i in d:
        h.append(i)
if(sorted(d)==sorted(h)):
    print("YES")
else:
    print("NO")
