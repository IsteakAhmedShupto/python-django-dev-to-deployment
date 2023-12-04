class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"

    def has_birthday(self):
        self.age += 1


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}"


brad = User('Brad Traversy', 'brad@gmail.com', 37)
janet = User('Janet Williams', 'janet@gmail.com', 27)

print(brad.name)
print(brad.email)
print(brad.age)

print(janet.name)
print(janet.email)
print(janet.age)

print(janet.greeting())

janet.has_birthday()

print(janet.age)

john = Customer('John Doe', 'john@gmail.com', 40)

john.set_balance(500)

print(john.balance)

print(john.greeting())
