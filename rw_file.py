employees_file= open('employees.txt', 'r+')
# print(employees_file.read())
for employee in employees_file.readlines():
    print(employee, end="")
employees_file.flush()
employees_file.close()