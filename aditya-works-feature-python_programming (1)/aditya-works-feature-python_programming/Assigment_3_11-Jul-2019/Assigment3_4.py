n=int(input("Input Number of elements: "))
sum=0
lis=[]
print("Input Elements :")
for i in range(n):
    lis.append(int(input()))

n1=int(input("Enter the number to be count : "))
print(lis.count(n1))
