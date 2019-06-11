N=int(input())
a=list(map(int,input().split()))
b=sorted(a)[::-1]
for i in b:
  print(i)
  
