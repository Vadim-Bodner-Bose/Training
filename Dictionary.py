#define a dictionary dictName = {key1: value1, key2: value2}
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)

#different method to access values in a dictionary, returns none for an unkonw value rather than throwing an error
print(student.get('name'))

#add a new value
student['phone'] = '555-5555'

# a way to modify multiple values in a dictionary
student.update({'name': 'Jane', 'age':26, 'phone':'555-5556'})
print student

#delete a value in a key using del

del student['age']
#anpother method to delete an antry in the dictionary while assigning it to a variable
name = student.pop('name')
print(name)
#check how many keys are in the dictionary
print(len(student))
#to check all keys in a dictionary
print(student.keys())
#to check all the values
print(student.values())
#to print keys and values
print(student.items())



