'''with open("sample.txt",'r') as file:
    output=file.readlines()'''
file=open('sample.txt','r')
output=[]
for i in file:
     print(i)
     output.append(i)

print("\n Content of first file is          :",output)

with open("sample1.txt",'w') as file:
    file.write(str(output[1::2])[1:-1])
print("\n Content of second file is          :",str(output[1::2])[1:-1])

with open("sample2.txt",'w') as file:
    file.write(str(output[::2])[1:-1])
print("\n Content of third file is          :",str(output[::2])[1:-1])



