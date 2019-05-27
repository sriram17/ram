a="aeiou"
b="abcdefghijklmnopqrstuvwxyz"
c=input()
if(c in b):
  if(c in a):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Invalid")
