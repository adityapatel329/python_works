import threading

def even(n,lock):
    sum = 0
    for i in n:
        if(i%2 == 0):
            sum = sum + i
    lock.acquire()
    print("Sum of even : ",sum)
    lock.release()

def odd(n,lock):
    sum = 0
    for i in n:
        if(i%2 !=0):
            sum = sum + i
    lock.acquire()
    print("Sum of odd : ",sum)
    lock.release()

if __name__ == "__main__":

    l1 = [1,2,3,4,5,6,7,8,9,10]
    lock = threading.Lock()

    t1 = threading.Thread(target = even,args =(l1,lock))
    t2 = threading.Thread(target = odd, args= (l1,lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
