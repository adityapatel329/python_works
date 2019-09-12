import threading
import time
def front(lock):
    lock.acquire()
    print("From front :")
    lock.release()
    for i in range(1,51):
        print(i)

def reverse(lock):
    lock.acquire()
    print("From reverse : ")
    lock.release()
    for i in range(1,51,-1):
        print(i)
        


if __name__ == "__main__":

    lock = threading.Lock()

    t1 = threading.Thread(target=front,args=(lock,))
    t2 = threading.Thread(target=reverse,args=(lock,))

    t1.start()
    time.sleep(2)
    t2.start()

    t1.join()
    t2.join()
