from marvellousnum import *
n=int(input("Input Number of elements: "))
sum=0
lis=[]
print("Input Elements :")
for i in range(n):
    lis.append(int(input()))

prime=marvellousnum.chkprime(lis)
print("Addition of prime nunmber : ",prime)
#def listprime():
