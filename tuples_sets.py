# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples','Oranges','Grapes')
fruits2 = tuple(('Apples','Oranges','Grapes'))

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
# del fruits2
print(fruits2)

# Get length
print(len(fruits))

print(fruits,fruits2)

# Single value needs trailing comma
fruits3 = ('Blueberries',) # Put trailing comma to ensure it is a tuple
print(fruits3,type(fruits3))

# A Set is a collection which is uordered and unindexed. No duplicate members.

# Craete set
fruits_set = {'Apples','Oranges','Mango'}

# Check if in set
print('Apples' in fruits_set) 

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Add duplicate
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)



# Delete set
# del fruits_set
print(fruits_set)