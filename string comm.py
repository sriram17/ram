N=int(input())
a=input()
k=""
b=[]
for i in range(0,N-1):
  s=input()
  for j in range(1,len(a)):
    if(a[0:j] in s ):
      k=a[0:j]
  b.append(k)
  k=""
m=b
count=0
for g in b:
    m.remove(g)
    for l in m:
        if(g in l):
            count=count+1
    if(count>=N//2):
        ans=g
    m=b
    count=0
print(ans)
    
    
