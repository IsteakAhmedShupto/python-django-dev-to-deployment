import json

userJSON = '{"first_name":"John","last_name":"Doe","age":30}'

user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'Ford',
       'model': 'Mustang',
       'year': 1970
       }

carJSON = json.dumps(car)

print(carJSON)
