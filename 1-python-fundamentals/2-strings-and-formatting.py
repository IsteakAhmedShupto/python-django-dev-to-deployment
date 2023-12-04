name = 'Brad'
age = 37

print('Hello World')

print('Hello' + name)

print('Hello I am' + name + ' am I am ' + str(age))

print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

print('My name is {name} and I am {age}'.format(name='Brad', age='37'))

print('My name is {name} and I am {age}'.format(name=name, age=age))

print('My name is {name} and I am {age}'.format(name='Brad', age='37'))

print(f"My name is {name} and I am {age}")

s = "hello there world"

print(s.capitalize())

print(s.upper())

print(s.lower())

print(s.swapcase())

print(len(s))

print(s.replace("world", "everyone"))

sub = "h"

print(s.count(sub))

print(s.startswith('hello'))

print(s.endswith('d'))

print(s.split())

print(s.find('r'))

print(s.isalnum())

print(s.isalpha())

print(s.isnumeric())
