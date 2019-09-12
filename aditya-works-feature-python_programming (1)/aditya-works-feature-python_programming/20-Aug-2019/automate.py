import os
import collections
import hashlib

class automate_file:
        templist = []
        duplicate = []
        checksum = {}
        fullpath = []
        def show_duplicate(self):
                
                name = input("Enter the root directory folder name : ")
                path = os.path.join('C:\\Users\\Public\\Downloads\\aditya-works\\Data',name)

                for root,dirs,files in os.walk(path):
                        for file_name in files:
                                #print(file_name)
                                self.templist.append(file_name)
                self.duplicate =[item for item, count in collections.Counter(self.templist).items() if count > 1]
                print("Duplicates files are : ")
                for i in self.duplicate:
                        print(str(i))

        def show_checksum(self):

                name = input("Enter the roor directory folder name : ")
                path = os.path.join('C:\\Users\\Public\\Downloads\\aditya-works\\Data',name)

                for root,dirs,files in os.walk(path):
                        for file_name in files:
                                self.templist.append(file_name)
                        for i in self.templist:
                                self.duplicate.append(hashlib.md5(i.encode("utf-8")).hexdigest())
                        for key in self.templist:
                                for value in self.duplicate:
                                        self.checksum[key] = value
                                        self.duplicate.remove(value)
                                        break
                print("Checksum with  files : ",self.checksum)

        def remove_duplicate(self):

                name = input("Enter the root directory folder name : ")
                path = os.path.join('C:\\Users\\Public\\Downloads\\aditya-works\\Data',name)
                for root,dirs,files in os.walk(path):
                        for file_name in files:
                               self.fullpath.append(os.path.join(root,file_name))

                for root,dirs,files in os.walk(path):
                        for file_name in files:
                                self.templist.append(file_name)
                self.duplicate =[item for item, count in collections.Counter(self.templist).items() if count > 1]
                print("Duplicate files are : ")
                for i in self.duplicate:
                        print(str(i))
                print("Removing the files : ")
                dictionary = dict(zip(self.duplicate,self.fullpath))
                for value in dictionary.values():
                        os.remove(value)
                        print("Removing .. ")
                
if __name__ == '__main__':
        obj = automate_file()
        while True:
                print("1. Show Duplicate files\n2. Show Checksum\n3. Remove Duplicate")
                choice = input("Enter your choice : ")
                if choice == '1':
                        obj.show_duplicate()
                elif choice == '2':
                        obj.show_checksum()
                elif choice == '3':
                        obj.remove_duplicate()
                else:
                        print("Wrong choice")
                        break
                        
                
