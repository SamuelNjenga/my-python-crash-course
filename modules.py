# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip manager (including Django) as well as custom modules.

# Core modules -> Available by default
import datetime
from datetime import date
import time
from time import time

# Pip module
import camelcase
from camelcase import CamelCase

# Import custom module
from validator import validate_email

c = CamelCase()
print(c.hump('hello there i like python'))

# today = datetime.date.today()
today  = date.today()
print(today)

# timestamp = time.time()
timestamp = time()
print(timestamp)


email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')    