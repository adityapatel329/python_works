from multiprocessing import Pool
def double(n):
   return n*2
if __name__=='__main__':
   pool=Pool(processes=3)
   result=pool.apply_async(double,(7,))
   print(result.get(timeout=1))
