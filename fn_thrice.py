a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
def sum_of_3(a,b,c):
    s=a+b+c
    if(a==b==c):
        return(3*s)
    else:
        return(s)
print("sum=",sum_of_3(a,b,c))
