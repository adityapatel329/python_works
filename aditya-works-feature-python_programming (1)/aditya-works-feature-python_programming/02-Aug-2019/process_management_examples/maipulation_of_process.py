from multiprocessing import *
import time

def target_process_1(run_statement):
    while True:
        if run_statement.value:
            print("I m running !")
            time.sleep(1)

def target_process_2(run_statement):
    time.sleep(3)
    print("Stoping")
    run_statement.value = False
    time.sleep(3)
    print("Resuming")
    run_statement = True

if __name__ == "__main__":

    run_statement = Value("i", 1)

    process_1 = Process(target = target_process_1, args = (run_statement,))
    process_2 = Process(target = target_process_2, args = (run_statement,))

    process_1.start()
    process_2.start()

   
