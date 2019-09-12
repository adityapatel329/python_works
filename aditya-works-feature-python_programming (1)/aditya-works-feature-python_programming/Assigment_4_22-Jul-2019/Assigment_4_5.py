from functools import reduce

l = []

n = int(input("Enter the limit : "))
print("Enter the elements : ")

for i in range(n):
    l.append(int(input()))

print("The list is : ",l)

prime =list(filter(lambda x: x %2 == 0, l))
print("prime number : ",prime)
        
mul = list(map(lambda x : x*2,prime))

print("Multiplication of two number : ",mul)

maximum = max(mul, key= lambda x: x)
print("Maximum of number",maximum)    

