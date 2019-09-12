class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but ca sink backwards.")

    def skeleton(self):
        print("The Shark's skeleton is made of cartilage.")

class Clownfish():
    def swim(self):
        print("The clownfish is swimming. ")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")

sam = Shark()
goldy = Clownfish()

for fish in (sam,goldy):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()

