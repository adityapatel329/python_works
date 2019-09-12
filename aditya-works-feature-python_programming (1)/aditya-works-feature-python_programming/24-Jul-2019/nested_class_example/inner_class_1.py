class Outer:

    def __init__(self):

        self.inner = self.Inner()

    def reveal(self):

        self.inner.display("Calling Inner class function from outer class")


    class Inner:
        def display(self,msg):
            print(msg)

outer = Outer()
outer.reveal()

## both method is right 

inner = outer.Inner() ## inner =Outer().Inner() or inner = outer.inner

inner.display("Just print it!")
