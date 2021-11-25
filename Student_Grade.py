m=int(input("Enter the mark of Maths"))
e=int(input("Enter the mark of English"))
s=int(input("Enter the mark of Science"))
h=int(input("Enter the mark of History"))
ml=int(input("Enter the mark of Malayalam"))
sum=m+e+s+h+ml
avg=(sum/5)*100
print("Sum=",sum)
print("Averge=",avg)
if avg>80:
    print("Grade A")
elif avg>60:
    print("Grade B")
elif avg>40:
    print("Grade C")
else:
    print("Failed")
