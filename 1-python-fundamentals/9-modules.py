# import datetime

# today = datetime.date.today()
# print(today)


import validator
import camelcase
from time import time
from datetime import date

today = date.today()
print(today)


timestamp = time()
print(timestamp)


camel = camelcase.CamelCase()

text = 'hello there world'

print(camel.hump(text))


email = 'test@test.com'

if validator.validate_email(email):
    print('Email is valid')
else:
    print('not an email')
