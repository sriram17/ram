a=input()
b=0
for i in a:
  b=b+int(i)**len(a)
if(a==str(b)):
  print("yes")
else:
  print("no")
