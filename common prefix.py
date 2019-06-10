N=int(input())
a=input()
for i in range(0,N-1):
  n=input()
  for j in range(1,len(a)):
    if(a[0:j] in n):
      com=a[0:j]
print(com)
