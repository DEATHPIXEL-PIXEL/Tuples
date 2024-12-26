tuple=(1,2,2,1)

e=len(tuple)-1
s=0
while s<e:
 if tuple[s]!= tuple[e]:
  print("it is not a palindrome")
  break
 s=s+1
 e=e-1
print("it is a palindrome")