import numpy
n=int(input("Input Number of elements: "))
sum=0
lis=[]
print("Input Elements :")
for i in range(n):
    lis.append(int(input()))

matrix(lis)
print(max(matrix))
for i in lis:
    if i>i+1:
        print(i)
    
