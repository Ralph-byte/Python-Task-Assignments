#This program determines person amd customer information
#main class
from mimetypes import init

from sqlalchemy import false


class Person:
    def __init__(self, name, address, telephone_no):
        self.name = name
        self.address = address
        self.telephone_no = telephone_no
        
#subclass for person
class Customer(Person):
    def __init__(self, name, address, telephone_no, customer_number, on_mail_list):
        super().__init__(name, address, telephone_no)
        
        #Initialize the production worker new attributes
        self.customer_number = customer_number
        self.on_mail_list = on_mail_list
        
        if self.on_mail_list ==True:
            self.on_mail_list = 'on a mail list'
        elif self.on_mail_list == False:
            self.on_mail_list = 'not on a mail list'
        # return self.on_mail_list      
        
         
         
         
         
#Creating object of the customer
cus = Customer('Ronney', 'Fiapre', 246780987, 2113, False)   

print("Name: " + cus.name)
print("Address: " + cus.address)
print("Telephone Number: " + str(cus.telephone_no))
print("Customer Number: " + str(cus.customer_number))
print("Customer Data: " + cus.on_mail_list) 
            
               
        
        