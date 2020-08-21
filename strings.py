# Strings in python are surrounded by either single or double quotation marks. String formatting and string methods


name  = 'Samuel'
age = 37

#Concatenate
print('Hello, my name is '+name+ ' and I am ' +str(age))
# Arguments by position
print('My name is {name} and I am {age}'.format(name=name,age=age))
# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')
#String Formatting

#String Methods
s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world','everyone'))

# Count
sub = 'o'
print(s.count(sub))

#Starts with 
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

k = 'Hey'

# Is all alphanumeric
print(k.isalnum())

# Is all alphabetic
print(k.isalpha())

# Is all numeric
print(k.isnumeric())

l = '600'
# Is all numeric
print(l.isnumeric())














