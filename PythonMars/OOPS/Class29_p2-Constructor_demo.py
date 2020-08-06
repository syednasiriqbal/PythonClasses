#### Time in Video 35:40, Before this he talked about Constructor ####

class Employee(object):
    
    def __init__(self):   # Constructor
        print("in constructor1 method")

    def employee_Detaills(self):  # Instance Methods 
        print("name of the person - Raja")
        
    def employee_Project_Info(self):   # Instance Methods 
        print("Project name is COBRA")
        
        
e=Employee()
e.employee_Detaills()
e.employee_Project_Info()
        
    

        