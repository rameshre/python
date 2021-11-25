a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c=int(input("Enter 1st Number"))
if a<b:
    if a<c:
        print(a," is smallest")
    else:
        print(c," is smallest")
elif b<c:
    print(b," is smallest")
else:
    print(c," is smallest")
