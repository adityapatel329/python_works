class BookStore:
    noofbooks = 0
    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.noofbooks = self.noofbook + 1

    def display(self):
        print(self.name)
        print(self.author)
        print("No of books : ",self.noofbooks)

if __name__ == "__main__":

    name = input("Enter book name : ")
    author = input("Enter author name : ")
    obj1 = BookStore(name,author)
    obj1.display()
    
    name1 = input("Enter book name : ")
    author1 = input("Enter author name : ")
    obj2 = BookStore(name1, author1)
    obj2.display()
