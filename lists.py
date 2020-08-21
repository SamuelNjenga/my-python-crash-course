# A List is a collection which is ordered  and changeable. Allows duplicate members.
# Similar to an array

# Create list
numbers = [1,2,3,4,5]

# Use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers,numbers2)

fruits = ['Apples','Oranges','Grapes','Pears']

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangoes')
print(fruits)

# Remove from list
fruits.remove('Oranges')

# Insert into position
fruits.insert(2,'StrawBerries')
print(fruits)

# Remove with pop
fruits.pop(1)

#Reverse list
fruits.reverse()

print(fruits)

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)
print(fruits)

fruits[0] = 'Blueberries'
print(fruits)


















