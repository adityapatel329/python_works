class Numbers:
    class Arithmetic:
        def __init__(self,value):
            self.value = value

        def chkprime(self):
            for i in range(2,self.value):
                if(i % self.value == 0):
                    return True

            else:
                return False

        def chkperfect(self):
            for i in range(self.value):
                if (i%i == 0):
                    return True
                else:
                    return False

        def facotrs(self):
            for i in range(self.value):
                
                if (i%i == 0):
                    print(i)
                else:
                    print("It is not a factor")
        def sumoffactors(self):
            
            
              for i in range(self.value):
                    sum = 0      
                    if (i%i == 0):
                        sum = sum + i
                        print(sum)
                    else:
                        print("It is not a factor")
if __name__ == "__main__":
    value = int(input("Enter your value :"))
    inner = Numbers
    outer = inner.Arithmetic(value)
    print(outer.chkprime())
    print(outer.chkperfect)
    outer.factors()
    outer.sumoffactors()
