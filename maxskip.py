n=int(input())
a=list(map(int,input().split()))
c=[]
pro=1
for i in a:
    pro=pro*i
    c.append(pro)
print(max(c))
