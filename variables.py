# A variable is  a container for a value, which can be of various types

'''
A multiline comment
'''
"""
VARIABLE RULES: 
 -Variable names are case sensitive
 -Must start with a letter or an underscore
 -Can have numbers but can not start with one
 """
 
x = 1    # int
y = 2.5  # float
name = 'John' # str
is_cool = True # bool
 
 #Multiple assignment -> More compact
x,y,name,is_cool = (1,2.5,'John',True)
print('Hello Three')
print(x,y,name,is_cool)

#Basic Math
p = x + y
print(p)

#Check Type
print(type(p))
print(type(x))

#Casting
x = str(x)
print(type(x))
y = int(y)
print(type(y),y) 