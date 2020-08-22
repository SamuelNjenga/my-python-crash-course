# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use identation with tabs or spaces

# Create function
def sayHello(name='Samwela'):
    print(f'Hello {name}')
    
sayHello('Sam Njenga')    

# Return values
def getSum(num1,num2):
    total = num1 + num2   
    return total

print(getSum(14,6))

num = getSum(12,88)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
getSum = lambda num1,num2 : num1 + num2
print(getSum(10,20))

getDiff = lambda num3, num4 : num3 - num4
print(getDiff(55,5))
