import threading


def even():
    print("First 10 even numbers : ")
    for i in range(1,11):
        if(i%2 == 0):
            print(i)

def odd():
    print("First 10 odd numbers : ")
    for i in range(1,11):
        if(i%2 != 0):
            print(i)

if __name__ == "__main__":

    

    t1 = threading.Thread(target = even())
    t2 = threading.Thread(target = odd())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    
