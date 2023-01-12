# A program for employee information
#Main purpose in to implement inheritance
#Main Class
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


#Subclass
class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(employee_name, employee_number)
        
        #Initialize the production worker new attributes
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate
        
    #method for setters(mutator)
    def set_ShiftNumber(self, shift_number):
        self.shift_number = shift_number
        
    def set_HourlyPayRate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate    
        
    #method for getters(accessor)
    def get_ShiftNumber(self):
        if self.shift_number == 1:
            self.shift_number = 'Day Shift'
        elif self.shift_number == 2:
            self.shift_number = 'Night Shift'
        else:
            print('Not a valid Shift')        
        return self.shift_number
    
    def get_HourlyPayRate(self):
        return self.hourly_pay_rate
    
#object for the production worker
# prod = Employee('James', 2113)
prod1 = ProductionWorker('James', 211134, 2, 12) 
print('Employee Name: ' +prod1.get_EmployeeName())
print('Employee Number: ' +str(prod1.get_EmployeeNumber()))
print('Shift Number: ' +str(prod1.get_ShiftNumber()))
print('Hourly Pay Rate: ' +str(prod1.get_HourlyPayRate()))
  
