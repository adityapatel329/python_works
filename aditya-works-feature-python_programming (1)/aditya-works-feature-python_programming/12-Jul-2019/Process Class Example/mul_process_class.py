from multiprocessing import Process
from time import sleep
square_result=[]
def calc_square(numbers):
    for n in numbers:
        global square_result
        
        print("square "+str(n*n))
        square_result.append(n*n)
    print("Result : " + str(square_result))

def calc_cube(numbers):
    for n in numbers:
        
        print("cube "+ str(n*n*n))
    
if __name__ == "__main__":
    arr=[2,3,8,9]
    p1 = Process(target=calc_square, args=(arr,))
    p2 = Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")
