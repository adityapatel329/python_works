def accept():
    name = input("Enter your string : ")
    val= []
    for i in name:
        
        val.append(ord(i))
    print(sum(val)/len(val))
    
accept()
