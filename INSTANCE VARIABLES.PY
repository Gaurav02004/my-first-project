# class Employee:
#   companyName = "Apple"
#   def__init__(self, name):
#   self.name = name 
#   def showDetails(self):
#     print(f"The name of the Employee is {self,name} and  the raise  amount is {self.raise_amount}")
       


# emp1 = Employee("Harry")
# emp1.raise_amount = 0.3
# emp1.showDetails()
# emp2 = Employee("Gaurav")
# emp2.showDetails()





# Employee.showDetails(emp1)
class Employee:
    companyName = "Apple"

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.0   # default value

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raise_amount}")


emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.showDetails()

emp2 = Employee("Gaurav")
emp2.showDetails()
