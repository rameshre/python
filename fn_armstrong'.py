n=int(input("Enter a number"))
x=n
def armstrong(n):
    a=s=0
    while(n>0):
        a=n%10
        s=s+(a*a*a)
        n=n//10
    return(s)
s=armstrong(n)
if(s==x):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
