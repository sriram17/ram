a,b=map(int,input().split())
c=[2,3,5,7,11,13]
k=[]
for i in range(a+1,b):
  if (i not in c):
    if((i%2!=0)and(i%3!=0)and(i%5!=0)and(i%7!=0)and(i%11!=0)and(i%13!=0)):
      k.append(i)
  else:
    k.append(i)
print(*k)
      
  
