k=int(input())
a=list(map(int,input().split()))
for i in range(0,k-1):
  n=list(map(int,input().split()))
  for j in n:
    if j not in a:
      a.append(j)
print(*sorted(a))
