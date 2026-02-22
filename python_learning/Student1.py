class Student:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def underage(self):
        if(self.age<18):
            print("under age")
