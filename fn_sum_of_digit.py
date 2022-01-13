n=int(input("Enter a number"))
def sum_of_digit(n):
    s=0
    while(n>0):
        a=n%10
        s=s+a
        n=n//10
    return(s)
Sum=sum_of_digit(n)
print("Sum=",Sum)
