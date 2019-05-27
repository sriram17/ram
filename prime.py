a=int(input())
b=[2,3,5,7,11]
if (a not in b):
  if((a%2!=0)and(a%3!=0)and(a%5!=0)and(a%7!=0)and(a%11!=0)and(a%13!=0)):
    print("yes")
  else:
    print("no")
else:
  print("yes")
