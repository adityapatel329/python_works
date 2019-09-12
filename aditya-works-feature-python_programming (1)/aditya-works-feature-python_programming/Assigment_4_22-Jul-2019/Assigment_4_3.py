from functools import reduce

l = []

n = int(input("Enter the limit : "))
print("Enter the elements : ")

for i in range(n):
    l.append(int(input()))

print("The list is : ",l)

greater = list(filter(lambda x : x>=70 and x<=90, l))

print("Greater number than 70 : ", greater)

increase = list(map(lambda x : x+10, greater))

print("The number is increase by 10 : ", increase)

product = reduce(lambda x,y : x*y,increase)

print("Product of the list : ", product)


