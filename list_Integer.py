l1=[2,3,4,5,6]
l2=[6,7,8,9,1]
c=0
len1=len(l1)
len2=len(l2)
print("Length of list1=",len1)
print( "Length of list2=",len2)
if(len1==len2):
    print("List have same length")
else:
    print("list have diferent length")
if(sum(l1)==sum(l2)):
    print("Sum of list are equal")

else:
    print("Sum of list are not equal")
for i in l1:
    for j in l2:
        if(i==j):
            c=c+1
            print("common elements=",i)

if(c==0):
    print("Common elements does not exist")
else:
    print("Common elements=",c)
