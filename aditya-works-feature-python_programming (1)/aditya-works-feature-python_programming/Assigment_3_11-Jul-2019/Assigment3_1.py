n=int(input("Input Number of elements: "))
sum=0
lis=[]
print("Input Elements :")
for i in range(n):
    lis.append(int(input()))

print(lis)
print(type(lis))
for i in lis:
    sum=sum+i


print("Addition :",sum)    

