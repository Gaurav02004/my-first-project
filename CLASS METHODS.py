# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name  is {self.name} and  company is {self.company}")

#         def changeCompany(cls, newCompany):
#             cls.company = newCompany

# e1 = Employee()
# e1.name = "Gaurav"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)  


# Class Methods as alternative constructor

# class Employee:
#     def__init__(self, name, salary):
#     self.name = name 
#     self.salary = salary

# e1 = Employee("Gaurav",12000)
# print(e1.name)
# print(e1.salary)


# string = "Gaurav-12000"
# e2 = Employee(string.split("_")[0], string.split("_")[1])
# print(e2.name)
# print(e2.salary)




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Gaurav", 12000)
print(e1.name)
print(e1.salary)


string = "Gaurav-12000"
data = string.split("-")

e2 = Employee(data[0], int(data[1]))
print(e2.name)
print(e2.salary)
