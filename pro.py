a=int(input())
x=0
n=0
s=[]
for i in range(1,a):
    j=str(i)
    for k in j:
        x=x+int(k)
    n=i+x
    if n==a:
        s.append(i)
    n=0
    x=0
print(len(s))
for j in s:
    print(j)
    
