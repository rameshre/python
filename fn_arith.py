a=int(input("Enter the 1st number"))
b=int(input("Enter the second number"))
def arith_ops(a,b):
    s=a+b
    m=a*b
    d=a-b
    div=a/b
    return(s,m,d,div)
l=arith_ops(a,b)
print("Sum=",l[0])
print("Product=",l[1])
print("Difference=",l[2])
print("Division=",l[3])


