# single-line comment

"""
Multi-line comment
"""

# x = 1  # int
# y = 2.5  # float
# name = 'Brad'  # string
# is_cool = True  # bool


x, y, name, is_cool = (1, 2.5, 'Brad', True)

print(x, y, name, is_cool)


a = x+y

print(a)


print(type(x))
print(type(y))
print(type(name))
print(type(is_cool))


x = str(x)
y = int(y)
z = float(y)

print(type(x))
print(type(y))
print(y)
print(type(z))
print(z)
