from Student1 import Student

class BE_Student(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
    def cgpa(self):
        return "8.4"
        
student= BE_Student("john", 13)
print(student.cgpa())