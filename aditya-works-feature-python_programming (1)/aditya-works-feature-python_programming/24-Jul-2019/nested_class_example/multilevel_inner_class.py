class Outer:

    def __init__(self):

        self.inner = self.Inner()

        self.innerinner = self.inner.InnerInner()


    def show_classes(self):
        print("This is outer class")
        print(inner)


    class Inner:

        def __init__(self):
            self.innerinner = self.InnerInner()

        def show_classes(self):
            print(self.innerinner)

        class InnerInner:

            def inner_display(self, msg):
                print("This is multilevel InnerInner class")
                print(msg)

        def inner_display(self, msg):
            print("This is Inner class")
            print(msg)

outer = Outer()
#outer.show_classes()

inner = outer.Inner()
inner.inner_display("Aditya")

print()

## this is 'InnerInner' class instance
innerinner = inner.InnerInner() ## innerinner = Outer().Inner().InnerInner()

## let's call its method inner_display
innerinner.inner_display("Just Print It!")
