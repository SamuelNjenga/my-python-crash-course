# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary so that we can work with it
# Also we may want to parse dictionary as JSON

import json

# Sample JSON
userJSON = '{"first_name":"John","last_name":"Njenga","age":22}'

# Parse to dict
user = json.loads(userJSON)
print(user) # Gives dictionary of user
print(user['age'])

# Python dictionary
react = {'language': 'JavaScript','styling': 'Material-UI','routing':'React-Router-DOM'}
# Dict to JSON
reactJSON = json.dumps(react) 
print(reactJSON)
