a,b=map(int,input().split())
r=0
c=[]
for i in range(a):
    c.append(list(map(int,input().split())))
for j in range(0,len(c)):
    if r in c[j]:
        c[j]=[0]*b
for k in c:
    print(k)
