nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

evens = list(filter(lambda n : n%2 == 0,nums))

doubles = list(map(lambda n : n*2,evens))

print("Even number of list : ",evens)

print("Double the number of list : ",doubles)


