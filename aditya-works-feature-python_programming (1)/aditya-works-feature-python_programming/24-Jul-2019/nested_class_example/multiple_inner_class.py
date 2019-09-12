class Outer:
    def __init__(self):
        self.inner = self.Inner()
        self._inner = self._Inner()

    def show_classes(self):
        print("This is Outer class")
        print(inner)
        print(_inner)

    class Inner:
        def inner_display(self, msg):
            print("This is Inner class")
            print(msg)

    class _Inner:
        def inner_display(self, msg):
            print("This is _Inner class")
            print(msg)

outer = Outer()

inner = outer.Inner()

_inner = outer._Inner()

outer.show_classes()
print()

inner.inner_display("Just Print It !")

print()

_inner.inner_display("Just Show It !")
