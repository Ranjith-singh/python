from Student1 import Student

class BE_Student(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
    def cgpa(self):
        return "8.4"

student= BE_Student("john", 13)
print(student.cgpa())

# li= [2, 2, 3, 5, 5]
# map= {}

# for i in li:
#     map[i]= map[i]+1
# for i in map.keys():
#     if map[i]>1:
#         print(i)