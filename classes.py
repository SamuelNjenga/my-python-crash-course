# A class is like a bluprint for creating objects. An object has properties and methods(functions) associated with it.
# Almost everything in Python is an object

# Create class
class User:
    # Constructor -> Function which runs when we first create an instance of a class i.e an Object of a class
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age += 1
        
        
# Extend class
class Customer(User):
    # Constructor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def set_balance(self,balance):
        self.balance = balance 
   
    def greeting(self):
     return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'      
# Init user object
sam = User('Samuel Njenga','snjenga@gmail.com',40)

#Init customer object
ivy = Customer('Ivy Wanjiku','ivy@gmail.com',22)
ivy.set_balance(400)

print(type(sam))        
print(sam.name)
print('Before Birthday I was ', sam.age)
sam.has_birthday()
print(sam.greeting())

print(ivy.greeting())