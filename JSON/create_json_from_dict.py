import json

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Seattle'
print(person_dict)
# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json)

# they look the same but they are not equal to python.!!!!
print(person_json == person_dict)