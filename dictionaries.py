# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-2222'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

print(person,type(person))

# Use constructor
person2 = dict(first_name='Sarah',last_name='Williams')
print(person2,type(person2))

# Copy dict
person3 = person.copy()
person3['city'] = 'Nairobi'

print(person3)

# Remove item
del(person3['age'])
person3.pop('phone')
print(person3)

# Get length
print(len(person3))

# Clear
person3.clear()
print(person3)

# List of dict
people = [
    {'name': 'Martha','age':30},
    {'name': 'Samuel','age':22}
]

print(people)
print(people[1]['name'])