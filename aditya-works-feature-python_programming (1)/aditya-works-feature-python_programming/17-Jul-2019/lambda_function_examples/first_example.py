def testfunc(num):
    return lambda x : x * num

result = testfunc(10)

print(result(9))
