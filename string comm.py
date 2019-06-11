N=int(input())
a=input()
k=""
for i in range(0,N-1):
  s=input()
  for j in range(0,len(a)):
    if(a[j] in s ):
      k=k+a[j]
      a=k
print(k)
