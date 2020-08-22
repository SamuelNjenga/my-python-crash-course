# If/ Else conditions are used to decide to do something based on something being true or false
x = 10
y = 10
# Comparison Operators (==, !=,>,<,>=,<=) -> Used to compare values
# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')     
    
# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y: 
    print(f'{x} is equal to {y}')  
else:
    print(f'{y} is greater than {x}')
        
        
# Nested if
z = 9
if z > 2:
    if z <= 10:
     print(f'{z} is greater than 2 and less than or equal to 10')        
     
# Logical operators (and, or, not) -> Used to combine conditional statements

# and
if z > 2 and z <= 10:
    print(f'{z} is greater than 2 and less than or equal to 10')     
    
# or    
if z > 2 or z <= 10:
    print(f'{z} is greater than 2 or less than or equal to 10')     
    
# not
h = 12
k = 98
if not(h == k):
    print(f'{h} is not equal to {k}')    
    
# Membership Operators (not, not in) -> Membership operators are used to test if a sequence is presented in an object.
# Test to see whether something is in a list.
numbers = [1,2,3,4,5,6]

# in
n = 2
if n in numbers:
    print(n in numbers)
    
# not in
if n not in numbers:
    print(n not in numbers)    
    
# Identify Operators (is, is not) -> Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
d = 's'
e = 's'
if d is e:
    print(d is e)    
    
# is not
d = 's'
e = 'S'
if d is not e:
    print(d is not e)    