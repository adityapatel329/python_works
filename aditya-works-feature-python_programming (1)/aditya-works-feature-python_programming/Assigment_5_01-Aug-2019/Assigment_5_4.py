def accept():
    name = input("Enter you string : ")
    n = int(input("Enter a position : "))
    l= []
    for i in name:
        l.append(i)
    #print(l)
    l.pop(n)
    for i in l:
        str(i)
        print(i,end="")
accept()
