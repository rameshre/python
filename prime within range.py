a=int(input("enter first number"))
b=int(input("Enter the second number"))
i=1
while(a<=b):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    if(c==2):
        print(a)
    a=a+1
        
