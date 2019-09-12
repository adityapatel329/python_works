add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice : "))

if choice == 1:
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter Second number : "))

    print("Addition : ",add(n1,n2))

elif choice == 2:
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter Second number : "))

    print("Subtraction : ",sub(n1,n2))

elif choice == 3:
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter Second number : "))

    print("Multiplication: ",mul(n1,n2))

elif choice == 4:
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter Second number : "))

    print("Division : ",div(n1,n2))
    
else:
    print("Wrong Input !!! ")
