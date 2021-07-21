import json

# Create a dictionary object
people_dict = {'first': 'Chris', 'last': 'Harry'}
# Add additional key pairs 
people_dict['City'] = 'Seattle'

# Convert dictionary to JSON
people_json = json.dumps(people_dict)
# print(people_json)

staff_dict = {}
# Add list to dictionary
staff_dict['Program manager'] = people_dict

# Convert the dictionary to JSON
staff_json = json.dumps(staff_dict)
print(staff_json)

# Read value of subkey
# refer to image json.png 
print(results['color']['dominantColorBackground'])

# To get everything listed in the tag section
for item in results['description']['tags']:
    print(item)