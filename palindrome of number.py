n=int(input("enter a number"))
p=n
s=a=0
while (n>0):
    a=n%10
    s=s*10+a
    n=n//10
if(p==s):
    print("palindrome")
else:
    print("not palindrome")

      
