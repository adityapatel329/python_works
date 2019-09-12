from functools import reduce

l = []

n = int(input("Enter the limit : "))
print("Enter the elements : ")

for i in range(n):
    l.append(int(input()))

print("The list is : ", l)

even = list(filter(lambda x: x % 2 == 0, l))

print("Enven number in a list : ", even)

square = list(map(lambda x: x * x, even))

print("Square for a given list : ", square)

product = reduce(lambda x, y: x + y, square)
print("Product of the list : ", product)
