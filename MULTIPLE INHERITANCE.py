class Employee:
    def __init__(self, name):
      self.name = name 

class Dancer:
    def __init__(self, dance):
        self.dance = dance

class DanceEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance = dance   
        self.name = name 
        o = DancerEmployee("Kathak", "Shivani") 
        print(o.name)
        print(o.dance)      
        o.show()         