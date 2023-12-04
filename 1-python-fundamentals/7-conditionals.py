x = 10
y = 6

if x == y:
    print(f'{x} is equal to {y}')


if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than or equal to {y}')


if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than to {y}')

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 but less than or equal to 10')


if x > 2 and x <= 10:
    print(f'{x} is greater than 2 but less than or equal to 10')

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 but less than or equal to 10')

if not (x == y):
    print(f'{x} is not equal to {y}')

x = 6

numbers = [1, 2, 3, 4, 5, 6]

if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x in numbers)

if x is y:
    print(x is y)

if x is not y:
    print(x is not y)
