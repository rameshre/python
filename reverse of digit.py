n=int(input("enter a number"))
s=a=0
while(n>0):
    a=n%10
    s=s*10+a
    n=n//10
print("reverse=",s)
    
