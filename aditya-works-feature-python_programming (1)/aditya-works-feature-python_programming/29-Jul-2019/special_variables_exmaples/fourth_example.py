class C:
    def f():
        pass
    class D:
        def g():
            pass

print(C.__qualname__)

print(C.f.__qualname__)

print(C.D.__qualname__)
