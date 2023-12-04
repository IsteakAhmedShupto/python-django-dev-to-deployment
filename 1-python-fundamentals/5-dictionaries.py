person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# person = dict(
#     first_name='John',
#     last_name='Doe',
#     age=30
# )


print(person)

print(person['first_name'])

print(person.get('last_name'))


person['phone'] = '555-555-5555'

print(person.keys())

print(person.items())

person2 = person.copy()

person2['city'] = 'Boston'

print(person2)

del (person['age'])

print(person)

person.pop('phone')

print(person)

print(len(person))

person.clear()

print(person)


people = [
    {'name': 'Martha', 'age': 40},
    {'name': 'Bob', 'age': 20},
]

print(people)

print(people[1])

print(people[1]['name'])
