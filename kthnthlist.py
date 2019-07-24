a,b=map(int,input().split())
c=list(map(int,input().split()))
d=sorted(c)[::-1]
print(d[b-1])
