import threading

def small(n):
    count = 0
    for i in (n):
        if(  i >= 97  and i <= 122):
            count = count + i
    print(count)

def capital(n):
    count = 0
    for i in ord(n):
        
        if( i>= 65 and i <= 95 ):
            count = count + i
    print(count)

def digits(n):
    count = 0
    for i in n:
        if( i>= 0 and i <= 100):
            count = count + i
    print(count)

if __name__ == "__main__":

    n = input("Enter a character : ")

    lock = threading.Lock()
    
    t1 = threading.Thread(target=small,args = (n,))
    t2 = threading.Thread(target=capital,args = (n,))
    t3 = threading.Thread(target=digits,args = (n,))
    
    t1.start()
    print()
    t2.start()
    print()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
