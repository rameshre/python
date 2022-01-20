l=[1,2,3,4,5,6,7,8,9,10,15]
for i in l:
    if(i%3==0 and i%5==0):
        print("C")
    elif(i%3==0):
         print("A")
    elif(i%5==0):
        print("B")

    else:
        print(i)
