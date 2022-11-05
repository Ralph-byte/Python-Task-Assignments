# A program to determine shift supervision 
#Main Class
from re import A


class Employee:
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number
        
    #method for setters(mutator)
    def set_EmployeeName(self, employee_name):
        self.employee_name = employee_name
        
    def set_EmployeeNumber(self, employee_number):
        self.employee_number = employee_number
        
    #method for getters(accessor)
    def get_EmployeeName(self):
        return self.employee_name
    
    def get_EmployeeNumber(self):
        return self.employee_number

# A subclass of the employee class    
class ShiftSupervisor(Employee):
    def __init__(self, employee_name, employee_number, annual_salary, annual_bonus):
        super().__init__(employee_name, employee_number)
        
        #Initialize the production worker new attributes
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus 
        
        
    #method for setters(mutator)
    def set_Salary(self, annual_salary):
        self.annual_salary = annual_salary
        
    def set_sBonus(self, annual_bonus):
        self.annual_bonus = annual_bonus
        
    
    #method for geeters(accessor) 
    def get_Salary(self):
        return self.annual_salary 
      
    def get_Bonus(self):
        return self.annual_bonus    
    
    
#object for the shift supervisor
super = ShiftSupervisor('Kalisto', 27913, 3800, 200)
print('Employee Name: ' +super.get_EmployeeName())
print('Employee Number: ' +str(super.get_EmployeeNumber()))
print('Annual Salary: ' +str(super.get_Salary()))
print('Annual Bonus: ' +str(super.get_Bonus()))