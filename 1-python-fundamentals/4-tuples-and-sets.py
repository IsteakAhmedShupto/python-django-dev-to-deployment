fruit_tuple = ('Apple', 'Orange', 'Mango')

fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

print(fruit_tuple)

print(fruit_tuple[1])

# cannot change value
# fruit_tuple[1] = 'Grape'

fruit_tuple_2 = ('Apple')

print(fruit_tuple_2)

# fruit_tuple_2 = ('Apple',)

# del fruit_tuple_2

# print(fruit_tuple_2)

print(len(fruit_tuple))

fruit_set = {'Apple', 'Orange', 'Mango'}

print(fruit_set)

print('Apple' in fruit_set)

fruit_set.add('Grape')

print(fruit_set)

fruit_set.remove('Grape')

print(fruit_set)

fruit_set.clear()

print(fruit_set)

# del fruit_set

# print(fruit_set)
