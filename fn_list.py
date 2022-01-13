l1=list(input("Enter the 1st list"))
l2=list(input("Enter the 2nd list"))
def fn_list(l1,l2):
    c=0
    for i in l1:
        for j in l2:
            if(i==j):
                return(True)
if(fn_list(l1,l2)):
    print("Common Elements Exist")
else:
    print("common elements does not exist")
