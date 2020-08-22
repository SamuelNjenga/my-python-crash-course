# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary,a set, or a string).

languages = ['Java','Python','JavaScript','C#','C++']

# Simple for loop
for language in languages:
    print(f'Current Person: {language}')

# Break -> Break out of the loop
for language in languages:
    if language == 'C#':
     break
    print(f'Current Person: {language}')
    
# Continue -> Continue in the loop after doing the skip
for language in languages:
    if language == 'C#':
     continue
    print(f'Current Person: {language}')
    
# range
for i in range(len(languages)):
    print(languages[i])        

for i in range(0,11):
    print(f'Number: {i}')
    
for i in range(0,16):
    if i % 2 == 0:
        print(f'Num is {i}')    
# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1