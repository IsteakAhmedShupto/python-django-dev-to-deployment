myFile = open('myfile.txt', 'w')

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

myFile.write("I love programming")
myFile.write(" and problem solving.")

myFile.close()

myFile = open("myfile.txt", 'a')
myFile.write(' I also like football.')
myFile.close()

myFile = open("myfile.txt", 'r+')
text = myFile.read(100)
print(text)
