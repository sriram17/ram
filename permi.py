from itertools import permutations
a=input()
b=permutations(a)
l=[]
k=[]
for i in list(b):
    g=list(i)
    f=int("".join(g))
    l.append(f)
for z in l:
    if z>int(a):
        k.append(z)
if len(k)==0:
    print("impossible")
else:
    print(min(k))

    
