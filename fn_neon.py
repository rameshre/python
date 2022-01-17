n=int(input("Enter the number"))
def neon(b):
    s=a=0
    q=(b**2)
    while(q>0):
        a=q%10
        s=s+a
        q=q//10
    if(s==b):
        print("The inputed number is Neon")
    else:
        print("The inputed number is not Neon")
neon(n)

        
    
